from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class StudentMessage(BaseModel):
    """Student's spoken input converted to text"""
    text: str = Field(..., description="Student's speech as text")
    session_id: str = Field(..., description="Unique session identifier")
    language: str = Field(default="tamil", description="Selected language code")

class CorrectionDetail(BaseModel):
    """Details of a grammar/usage correction"""
    is_correct: bool
    corrected_sentence: Optional[str] = None
    explanation: Optional[str] = None
    mistake_type: Optional[str] = None  # grammar, word_choice, pronunciation, etc.

class TutorResponse(BaseModel):
    """Tutor's response to student"""
    text: str = Field(..., description="Tutor's spoken response")
    correction: Optional[CorrectionDetail] = None
    encouragement: str = Field(..., description="Positive reinforcement message")
    should_repeat: bool = Field(default=False, description="Whether student should repeat")
    
class ConversationTurn(BaseModel):
    """Single turn in conversation history"""
    timestamp: str
    student_text: str
    tutor_response: str
    had_correction: bool

class SessionData(BaseModel):
    """Student session tracking"""
    session_id: str
    started_at: str
    conversation_history: List[ConversationTurn] = []
    corrections_count: int = 0
    successful_repetitions: int = 0
    total_turns: int = 0
    current_difficulty: str = "beginner"  # beginner, intermediate, advanced
    
class SessionStats(BaseModel):
    """Session statistics for progress tracking"""
    total_corrections: int
    successful_repetitions: int
    conversation_length: int
    improvement_rate: float
