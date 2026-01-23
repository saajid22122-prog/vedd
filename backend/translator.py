"""
Translation utility using Deep Translator
Provides automatic translation for UI text and dynamic content
"""

from deep_translator import GoogleTranslator
from typing import Dict, Optional

# Language code mapping (Deep Translator uses ISO codes)
LANGUAGE_CODES = {
    'tamil': 'ta',
    'hindi': 'hi',
    'telugu': 'te',
    'malayalam': 'ml',
    'kannada': 'kn',
    'bengali': 'bn'
}

def translate_text(text: str, target_language: str, source_language: str = 'en') -> str:
    """
    Translate text to target language using Google Translate (via Deep Translator)
    
    Args:
        text: Text to translate
        target_language: Target language code (tamil, hindi, etc.)
        source_language: Source language code (default: en)
    
    Returns:
        Translated text
    """
    try:
        target_code = LANGUAGE_CODES.get(target_language, 'ta')
        translator = GoogleTranslator(source=source_language, target=target_code)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return original if translation fails

def batch_translate(texts: Dict[str, str], target_language: str) -> Dict[str, str]:
    """
    Translate multiple texts at once
    
    Args:
        texts: Dictionary of key-value pairs to translate
        target_language: Target language code
    
    Returns:
        Dictionary with translated values
    """
    translated = {}
    for key, text in texts.items():
        translated[key] = translate_text(text, target_language)
    return translated

def auto_generate_language_config(language: str) -> Dict:
    """
    Auto-generate language configuration using translation
    Useful for adding new languages quickly
    
    Args:
        language: Language name in English (e.g., 'Gujarati', 'Marathi')
    
    Returns:
        Complete language configuration dictionary
    """
    
    # Base English text to translate
    base_config = {
        "praise": [
            "Exactly right!",
            "Excellent!",
            "Very good!",
            "Great!",
            "Super!"
        ],
        "encouragement": [
            "Good try",
            "Good effort",
            "Even better next time",
            "Keep trying"
        ],
        "ui": {
            "welcome": "Hello!",
            "teacher_intro": "I am your language teacher!",
            "click_to_speak": "Click the mic and start speaking",
            "listening": "Listening...",
            "speaking": "Teacher is speaking...",
            "click_mic": "Click to speak",
            "full_sentence": "Say the full sentence",
            "repeat_now": "Now you say it.",
            "correct_sentence": "Correct sentence:",
            "corrections": "Corrections:",
            "your_progress": "Your progress",
            "total_conversations": "Total conversations",
            "corrections_count": "Corrections",
            "accuracy_percent": "Accuracy percentage"
        }
    }
    
    # Translate all phrases
    config = {
        "praise": [translate_text(p, language) for p in base_config["praise"]],
        "encouragement": [translate_text(e, language) for e in base_config["encouragement"]],
        "ui": {}
    }
    
    # Translate UI text
    for key, value in base_config["ui"].items():
        config["ui"][key] = translate_text(value, language)
    
    return config

# Example usage for generating new language
if __name__ == "__main__":
    # Test translation
    print("Testing translation...")
    print(translate_text("Good job!", "tamil"))
    print(translate_text("Try again", "hindi"))
    print(translate_text("Excellent!", "telugu"))
