from typing import Dict, List
from datetime import datetime
from models import SessionData, ConversationTurn, TutorResponse, CorrectionDetail
from groq_client import GroqClient
from language_config import get_language_config
import random

class TutorEngine:
    """
    Core AI Voice Tutor Engine implementing the 21 behavioral rules
    Supports multiple Indian languages
    """
    
    def __init__(self, language="tamil"):
        self.groq_client = GroqClient()
        self.sessions: Dict[str, SessionData] = {}
        self.language = language
        self.lang_config = get_language_config(language)
        
        # Get language-specific phrases
        self.praise_phrases = self.lang_config["praise"]
        self.encouragement_phrases = self.lang_config["encouragement"]
        self.ui_text = self.lang_config["ui"]
        self.language_name = self.lang_config["english_name"]
        
        self.system_prompt = f"""You are a friendly {self.language_name} language tutor for children aged 5-15.

CRITICAL RULES:
1. Always respond in {self.language_name} ({self.lang_config['name']})
2. Keep responses SHORT - maximum 2-3 sentences
3. Sound like a warm, encouraging human tutor, NOT a robot
4. Never give long explanations
5. Always maintain natural conversation flow
6. Focus on ONE correction at a time
7. After praising or correcting, ask a simple follow-up question to continue conversation

BEHAVIOR:
- If student speaks correctly: Praise briefly + ask related question
- If student makes mistake: You will receive separate correction details
- If student gives short answer (one word): Ask them to make a full sentence
- Always be positive and encouraging
- Adapt difficulty based on student performance

Remember: You are having a conversation, not giving a grammar lesson!"""

    def get_or_create_session(self, session_id: str) -> SessionData:
        """Get existing session or create new one"""
        if session_id not in self.sessions:
            self.sessions[session_id] = SessionData(
                session_id=session_id,
                started_at=datetime.now().isoformat(),
                conversation_history=[],
                corrections_count=0,
                successful_repetitions=0,
                total_turns=0,
                current_difficulty="beginner"
            )
        return self.sessions[session_id]
    
    def process_student_input(self, student_text: str, session_id: str) -> TutorResponse:
        """
        Main processing function - implements the core tutoring logic
        
        Following the 21 rules from specification
        """
        session = self.get_or_create_session(session_id)
        
        # Rule 11: Check for very short answers
        if len(student_text.strip().split()) <= 2 and session.total_turns > 0:
            return TutorResponse(
                text="Please say the full sentence 🙂",
                correction=None,
                encouragement="",
                should_repeat=False
            )
        
        # Analyze grammar using AI with language specification
        grammar_analysis = self.groq_client.analyze_grammar(
            student_text, 
            self.language_name
        )
        
        is_correct = grammar_analysis.get("is_correct", True)
        
        if is_correct:
            # Rule 2: Student speech is CORRECT
            response = self._handle_correct_response(student_text, session)
        else:
            # Rule 3: Student speech is INCORRECT - follow exact sequence
            response = self._handle_incorrect_response(
                student_text, 
                grammar_analysis, 
                session
            )
        
        # Update session
        session.total_turns += 1
        session.conversation_history.append(
            ConversationTurn(
                timestamp=datetime.now().isoformat(),
                student_text=student_text,
                tutor_response=response.text,
                had_correction=not is_correct
            )
        )
        
        # Rule 19: Adapt difficulty
        self._adapt_difficulty(session)
        
        return response
    
    def _handle_correct_response(self, student_text: str, session: SessionData) -> TutorResponse:
        """Rule 2: Praise briefly and ask follow-up question"""
        
        # Get conversation context
        conversation_history = self._format_history_for_ai(session)
        
        # Praise phrase
        praise = random.choice(self.praise_phrases)
        
        # Generate natural follow-up using AI
        prompt = f"Student said: {student_text}\n\nGive a brief follow-up question to continue the conversation naturally. Keep it simple for a child."
        
        follow_up = self.groq_client.generate_tutor_response(
            student_input=student_text,
            conversation_history=conversation_history,
            system_prompt=self.system_prompt
        )
        
        # Combine praise and follow-up
        full_response = f"{praise} {follow_up}"
        
        return TutorResponse(
            text=full_response,
            correction=None,
            encouragement=praise,
            should_repeat=False
        )
    
    def _handle_incorrect_response(
        self, 
        student_text: str, 
        grammar_analysis: Dict,
        session: SessionData
    ) -> TutorResponse:
        """
        Rule 3: Follow exact sequence for corrections with detailed word-level feedback
        IMPORTANT: Response in ENGLISH when student makes mistakes (for clarity)
        
        Step 1: Acknowledge effort positively
        Step 2: Provide correct sentence
        Step 3: Give ONE short explanation (now with word-level details)
        Step 4: Ask student to repeat
        """
        
        # Use English phrases for corrections
        encouragement_english = [
            "Good try! 🙂",
            "Nice effort! 💪",
            "You're getting better! 🌈",
            "Keep practicing! 🎯"
        ]
        
        encouragement = random.choice(encouragement_english)
        corrected = grammar_analysis.get("corrected_sentence", student_text)
        explanation = grammar_analysis.get("explanation", "")
        word_corrections = grammar_analysis.get("word_corrections", [])
        
        # Build detailed response in ENGLISH
        response_parts = [encouragement]
        
        # Show corrected sentence
        response_parts.append(f"Correct sentence: {corrected}")
        
        # If we have word-level corrections, show them
        if word_corrections and len(word_corrections) > 0:
            response_parts.append("\nCorrections:")
            for i, correction in enumerate(word_corrections[:2], 1):  # Show max 2 word corrections
                original = correction.get("original", "")
                correct_word = correction.get("corrected", "")
                reason = correction.get("reason", "")
                
                if original and correct_word:
                    response_parts.append(f"• '{original}' → '{correct_word}' ({reason})")
        elif explanation:
            # Fallback to general explanation if no word corrections
            response_parts.append(explanation)
        
        response_parts.append("\nNow you try saying it.")
        
        full_response = "\n".join(response_parts)
        
        # Create detailed correction object
        correction = CorrectionDetail(
            is_correct=False,
            corrected_sentence=corrected,
            explanation=explanation if not word_corrections else "Word-level corrections provided",
            mistake_type=grammar_analysis.get("mistake_type", "grammar")
        )
        
        # Update stats
        session.corrections_count += 1
        
        return TutorResponse(
            text=full_response,
            correction=correction,
            encouragement=encouragement,
            should_repeat=True
        )
    
    def _format_history_for_ai(self, session: SessionData) -> List[Dict[str, str]]:
        """Format conversation history for AI context"""
        history = []
        for turn in session.conversation_history[-5:]:  # Last 5 turns
            history.append({"role": "user", "content": turn.student_text})
            history.append({"role": "assistant", "content": turn.tutor_response})
        return history
    
    def _adapt_difficulty(self, session: SessionData):
        """Rule 19: Adapt difficulty based on performance"""
        if session.total_turns < 5:
            return  # Too early to adapt
        
        error_rate = session.corrections_count / session.total_turns
        
        if error_rate < 0.2 and session.current_difficulty == "beginner":
            session.current_difficulty = "intermediate"
        elif error_rate > 0.5 and session.current_difficulty == "intermediate":
            session.current_difficulty = "beginner"
        elif error_rate < 0.1 and session.current_difficulty == "intermediate":
            session.current_difficulty = "advanced"
    
    def get_session_stats(self, session_id: str) -> Dict:
        """Get statistics for a session"""
        session = self.get_or_create_session(session_id)
        
        improvement_rate = 0.0
        if session.total_turns > 0:
            improvement_rate = (1 - (session.corrections_count / session.total_turns)) * 100
        
        return {
            "total_corrections": session.corrections_count,
            "successful_repetitions": session.successful_repetitions,
            "conversation_length": session.total_turns,
            "improvement_rate": round(improvement_rate, 1),
            "current_difficulty": session.current_difficulty
        }
