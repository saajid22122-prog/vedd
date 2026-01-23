"""
Test the tutor response logic with English for mistakes
"""
import sys
sys.path.append('.')

from tutor_engine import TutorEngine

def test_responses():
    """Test response language logic"""
    
    print("="*80)
    print("TESTING RESPONSE LANGUAGE LOGIC")
    print("="*80)
    
    # Test Tamil tutor
    print("\n--- TAMIL TUTOR ---\n")
    tamil_tutor = TutorEngine(language="tamil")
    
    # Test 1: Incorrect sentence (should be in English)
    print("Test 1: Incorrect sentence (mixed language)")
    print("Student: நான் school போனேன்")
    response = tamil_tutor.process_student_input("நான் school போனேன்", "test_session_1")
    print(f"\nTutor Response:\n{response.text}\n")
    print("-"*80)
    
    # Test 2: Correct sentence (should be in Tamil)
    print("\nTest 2: Correct sentence")
    print("Student: நான் பள்ளிக்கு போனேன்")
    response = tamil_tutor.process_student_input("நான் பள்ளிக்கு போனேன்", "test_session_2")
    print(f"\nTutor Response:\n{response.text}\n")
    print("-"*80)
    
    # Test Hindi tutor
    print("\n--- HINDI TUTOR ---\n")
    hindi_tutor = TutorEngine(language="hindi")
    
    # Test 3: Incorrect sentence (should be in English)
    print("Test 3: Incorrect sentence (mixed language)")
    print("Student: मैं school जाता हूं")
    response = hindi_tutor.process_student_input("मैं school जाता हूं", "test_session_3")
    print(f"\nTutor Response:\n{response.text}\n")
    print("-"*80)
    
    # Test 4: Correct sentence (should be in Hindi)
    print("\nTest 4: Correct sentence")
    print("Student: मैं स्कूल जाता हूं")
    response = hindi_tutor.process_student_input("मैं स्कूल जाता हूं", "test_session_4")
    print(f"\nTutor Response:\n{response.text}\n")
    print("-"*80)
    
    print("\n✅ Tests completed!")
    print("\nExpected behavior:")
    print("- Incorrect answers: Response in English")
    print("- Correct answers: Response in native language")

if __name__ == "__main__":
    test_responses()
