import os
from groq import Groq
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class GroqClient:
    """Wrapper for Groq API to generate tutor responses"""
    
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile"  # Current supported Groq model
        
    def generate_tutor_response(
        self, 
        student_input: str,
        conversation_history: List[Dict[str, str]],
        system_prompt: str
    ) -> str:
        """
        Generate AI tutor response based on student input and conversation history
        
        Args:
            student_input: What the student said
            conversation_history: Previous conversation turns
            system_prompt: System instructions for tutor behavior
            
        Returns:
            Generated tutor response
        """
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add conversation history
        for turn in conversation_history[-5:]:  # Last 5 turns for context
            messages.append(turn)
        
        # Add current student input
        messages.append({"role": "user", "content": student_input})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,  # Balanced creativity
                max_tokens=300,   # Keep responses concise
                top_p=0.9
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Groq API Error: {e}")
            return "மன்னிக்கவும், எனக்கு சிறிது சிக்கல் உள்ளது. மீண்டும் முயற்சி செய்."
    
    def analyze_grammar(
        self,
        student_sentence: str,
        expected_language: str = "Tamil"
    ) -> Dict:
        """
        Analyze grammar with detailed word-level parsing and corrections
        
        Returns dict with:
        - is_correct: bool
        - corrected_sentence: str (if needed)
        - explanation: str (if correction needed)
        - word_corrections: list of specific word fixes
        """
        system_prompt = f"""You are a precise {expected_language} grammar analyzer for children aged 5-15.

Analyze the student's sentence word-by-word and respond in valid JSON format with proper escaping:

{{
    "is_correct": true or false,
    "corrected_sentence": "the fully corrected sentence in {expected_language}",
    "explanation": "one simple sentence in ENGLISH explaining the main mistake (empty if correct)",
    "mistake_type": "grammar" or "word_choice" or "mixed_language" or "structure" or "pronunciation" or null,
    "word_corrections": [
        {{
            "original": "incorrect word",
            "corrected": "correct word in {expected_language}",
            "reason": "brief explanation in ENGLISH"
        }}
    ]
}}

CRITICAL RULES:
1. Check each word individually for correctness
2. Detect mixed language usage (English words in {expected_language} sentences)
3. Verify proper {expected_language} grammar particles and markers
4. Check verb conjugations and tense agreement
5. Identify word order issues
6. EXPLANATIONS AND REASONS MUST BE IN ENGLISH (for learning)
7. CORRECTED TEXT MUST BE IN {expected_language} (for practice)
8. Mark is_correct=true ONLY if sentence is completely correct
9. If correcting, ensure corrected_sentence is natural {expected_language}
10. word_corrections should list ALL words that need fixing
11. Keep explanations simple and child-friendly in English
12. Escape all special characters in JSON properly

Examples:
Input: "நான் school போனேன்" (Tamil with English word)
Output: {{
    "is_correct": false,
    "corrected_sentence": "நான் பள்ளிக்கு போனேன்",
    "explanation": "Use the Tamil word for 'school' instead of English",
    "mistake_type": "mixed_language",
    "word_corrections": [
        {{
            "original": "school",
            "corrected": "பள்ளிக்கு",
            "reason": "English word used; use Tamil word with location marker 'க்கு'"
        }}
    ]
}}

Input: "நான் பள்ளி போனேன்" (Missing location particle)
Output: {{
    "is_correct": false,
    "corrected_sentence": "நான் பள்ளிக்கு போனேன்",
    "explanation": "Need to add location marker 'க்கு' when going to a place",
    "mistake_type": "grammar",
    "word_corrections": [
        {{
            "original": "பள்ளி",
            "corrected": "பள்ளிக்கு",
            "reason": "Location marker 'க்கு' needed for indicating destination"
        }}
    ]
}}

Input (Hindi): "मैं school जाता हूं"
Output: {{
    "is_correct": false,
    "corrected_sentence": "मैं स्कूल जाता हूं",
    "explanation": "Use the Hindi word for 'school' instead of English",
    "mistake_type": "mixed_language",
    "word_corrections": [
        {{
            "original": "school",
            "corrected": "स्कूल",
            "reason": "English word used; replace with Hindi word"
        }}
    ]
}}"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analyze this sentence carefully: {student_sentence}"}
                ],
                temperature=0.2,  # Very deterministic for accurate grammar analysis
                max_tokens=500,
                response_format={"type": "json_object"}
            )
            
            import json
            result = json.loads(response.choices[0].message.content)
            
            # Ensure all required fields exist
            if "word_corrections" not in result:
                result["word_corrections"] = []
            
            # Validate the response
            if not isinstance(result.get("is_correct"), bool):
                result["is_correct"] = True
            
            if not result.get("corrected_sentence"):
                result["corrected_sentence"] = student_sentence
                
            if not result.get("explanation"):
                result["explanation"] = ""
            
            return result
            
        except Exception as e:
            print(f"Grammar analysis error: {e}")
            # Default to accepting if analysis fails
            return {
                "is_correct": True,
                "corrected_sentence": student_sentence,
                "explanation": "",
                "mistake_type": None,
                "word_corrections": []
            }
