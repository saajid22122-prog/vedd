from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import StudentMessage, TutorResponse, SessionStats
from tutor_engine import TutorEngine
from language_config import get_available_languages
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AI Voice Tutor API",
    description="Real-time voice tutoring for children learning Indian languages",
    version="2.0.0"
)

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:5173")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize tutor engines for each language (lazy loading)
tutors = {}

def get_tutor(language: str) -> TutorEngine:
    """Get or create tutor engine for a specific language"""
    if language not in tutors:
        tutors[language] = TutorEngine(language=language)
    return tutors[language]

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "AI Voice Tutor",
        "version": "2.0.0",
        "supported_languages": len(get_available_languages())
    }

@app.get("/languages")
async def get_languages():
    """Get list of supported languages"""
    return {
        "languages": get_available_languages()
    }

@app.post("/chat", response_model=TutorResponse)
async def process_message(message: StudentMessage):
    """
    Process student's spoken message and return tutor response
    
    This endpoint:
    1. Receives student's speech (as text from STT)
    2. Analyzes grammar and correctness in the selected language
    3. Generates appropriate tutor response following behavioral rules
    4. Returns response for TTS to speak
    """
    try:
        if not message.text.strip():
            raise HTTPException(status_code=400, detail="Empty message")
        
        # Get tutor for the selected language
        tutor = get_tutor(message.language)
        
        response = tutor.process_student_input(
            student_text=message.text,
            session_id=message.session_id
        )
        
        return response
        
    except Exception as e:
        print(f"Error processing message: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/session/{session_id}/stats", response_model=SessionStats)
async def get_session_stats(session_id: str, language: str = "tamil"):
    """
    Get statistics and progress for a student session
    
    Returns:
    - Total corrections made
    - Successful repetitions
    - Conversation length
    - Improvement rate
    """
    try:
        tutor = get_tutor(language)
        stats = tutor.get_session_stats(session_id)
        return SessionStats(**stats)
        
    except Exception as e:
        print(f"Error fetching stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/session/{session_id}")
async def end_session(session_id: str, language: str = "tamil"):
    """End a session and clean up"""
    tutor = get_tutor(language)
    if session_id in tutor.sessions:
        del tutor.sessions[session_id]
        return {"message": "Session ended successfully"}
    return {"message": "Session not found"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("BACKEND_PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
