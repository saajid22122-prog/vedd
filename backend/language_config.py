"""
Language configuration for multi-language support
Supports: Tamil, Hindi, Telugu, Malayalam, Kannada, Bengali
"""

SUPPORTED_LANGUAGES = {
    "tamil": {
        "name": "தமிழ்",
        "english_name": "Tamil",
        "code": "ta",
        "speech_code": "ta-IN",
        "flag": "🇮🇳",
        
        # Praise phrases
        "praise": [
            "சரியாக சொன்னாய்! 👏",
            "அருமை! 🌟",
            "நல்லா சொன்னாய்! 😊",
            "பரவாயில்லை! 👍",
            "சூப்பர்! ⭐"
        ],
        
        # Encouragement phrases
        "encouragement": [
            "நல்ல முயற்சி 🙂",
            "நல்லா முயற்சி செய்தாய் 💪",
            "இன்னும் நல்லா வரும் 🌈",
            "தொடர்ந்து முயற்சி செய் 🎯"
        ],
        
        # UI text
        "ui": {
            "welcome": "வணக்கம்! 🙏",
            "teacher_intro": "நான் உன் தமிழ் teacher! 👨‍🏫",
            "click_to_speak": "மைக்கை click செய்து பேச தொடங்கு",
            "listening": "கேட்கிறேன்...",
            "speaking": "Teacher பேசுகிறார்...",
            "click_mic": "பேச Click செய்",
            "full_sentence": "முழு வாக்கியமாக சொல்லு 🙂",
            "repeat_now": "இப்போ நீ சொல்லு.",
            "correct_sentence": "சரியான வாக்கியம்:",
            "corrections": "திருத்தங்கள்:",
            "your_progress": "உன் முன்னேற்றம் 📊",
            "total_conversations": "மொத்த உரையாடல்கள்",
            "corrections_count": "திருத்தங்கள்",
            "accuracy_percent": "சரியான சதவீதம்"
        }
    },
    
    "hindi": {
        "name": "हिंदी",
        "english_name": "Hindi",
        "code": "hi",
        "speech_code": "hi-IN",
        "flag": "🇮🇳",
        
        "praise": [
            "बिल्कुल सही! 👏",
            "शाबाश! 🌟",
            "बहुत अच्छा! 😊",
            "वाह! 👍",
            "सुपर! ⭐"
        ],
        
        "encouragement": [
            "अच्छी कोशिश 🙂",
            "बहुत अच्छी कोशिश की 💪",
            "और भी बेहतर होगा 🌈",
            "कोशिश करते रहो 🎯"
        ],
        
        "ui": {
            "welcome": "नमस्ते! 🙏",
            "teacher_intro": "मैं आपका हिंदी teacher हूँ! 👨‍🏫",
            "click_to_speak": "माइक पर क्लिक करें और बोलना शुरू करें",
            "listening": "सुन रहा हूँ...",
            "speaking": "Teacher बोल रहा है...",
            "click_mic": "बोलने के लिए क्लिक करें",
            "full_sentence": "पूरा वाक्य बोलें 🙂",
            "repeat_now": "अब आप बोलें।",
            "correct_sentence": "सही वाक्य:",
            "corrections": "सुधार:",
            "your_progress": "आपकी प्रगति 📊",
            "total_conversations": "कुल बातचीत",
            "corrections_count": "सुधार",
            "accuracy_percent": "सही प्रतिशत"
        }
    },
    
    "telugu": {
        "name": "తెలుగు",
        "english_name": "Telugu",
        "code": "te",
        "speech_code": "te-IN",
        "flag": "🇮🇳",
        
        "praise": [
            "చాలా బాగా చెప్పావు! 👏",
            "అద్భుతం! 🌟",
            "బాగుంది! 😊",
            "చక్కగా ఉంది! 👍",
            "సూపర్! ⭐"
        ],
        
        "encouragement": [
            "మంచి ప్రయత్నం 🙂",
            "బాగా ప్రయత్నించావు 💪",
            "ఇంకా మెరుగ్గా వస్తుంది 🌈",
            "ప్రయత్నం కొనసాగించు 🎯"
        ],
        
        "ui": {
            "welcome": "నమస్కారం! 🙏",
            "teacher_intro": "నేను మీ తెలుగు teacher! 👨‍🏫",
            "click_to_speak": "మైక్ మీద క్లిక్ చేసి మాట్లాడటం ప్రారంభించండి",
            "listening": "వింటున్నాను...",
            "speaking": "Teacher మాట్లాడుతున్నారు...",
            "click_mic": "మాట్లాడటానికి క్లిక్ చేయండి",
            "full_sentence": "పూర్తి వాక్యం చెప్పండి 🙂",
            "repeat_now": "ఇప్పుడు మీరు చెప్పండి।",
            "correct_sentence": "సరైన వాక్యం:",
            "corrections": "దిద్దుబాట్లు:",
            "your_progress": "మీ పురోగతి 📊",
            "total_conversations": "మొత్తం సంభాషణలు",
            "corrections_count": "దిద్దుబాట్లు",
            "accuracy_percent": "సరైన శాతం"
        }
    },
    
    "malayalam": {
        "name": "മലയാളം",
        "english_name": "Malayalam",
        "code": "ml",
        "speech_code": "ml-IN",
        "flag": "🇮🇳",
        
        "praise": [
            "ശരിയായി പറഞ്ഞു! 👏",
            "വളരെ നന്ന്! 🌟",
            "നല്ലത്! 😊",
            "കൊള്ളാം! 👍",
            "സൂപ്പർ! ⭐"
        ],
        
        "encouragement": [
            "നല്ല ശ്രമം 🙂",
            "നല്ല ശ്രമം നടത്തി 💪",
            "കൂടുതൽ നന്നായി വരും 🌈",
            "ശ്രമം തുടരുക 🎯"
        ],
        
        "ui": {
            "welcome": "നമസ്കാരം! 🙏",
            "teacher_intro": "ഞാൻ നിങ്ങളുടെ മലയാളം teacher! 👨‍🏫",
            "click_to_speak": "മൈക്ക് ക്ലിക്ക് ചെയ്ത് സംസാരിക്കാൻ തുടങ്ങുക",
            "listening": "കേൾക്കുന്നു...",
            "speaking": "Teacher സംസാരിക്കുന്നു...",
            "click_mic": "സംസാരിക്കാൻ ക്ലിക്ക് ചെയ്യുക",
            "full_sentence": "പൂർണ്ണ വാക്യം പറയുക 🙂",
            "repeat_now": "ഇപ്പോൾ നിങ്ങൾ പറയുക.",
            "correct_sentence": "ശരിയായ വാക്യം:",
            "corrections": "തിരുത്തലുകൾ:",
            "your_progress": "നിങ്ങളുടെ പുരോഗതി 📊",
            "total_conversations": "മൊത്തം സംഭാഷണങ്ങൾ",
            "corrections_count": "തിരുത്തലുകൾ",
            "accuracy_percent": "ശരിയായ ശതമാനം"
        }
    },
    
    "kannada": {
        "name": "ಕನ್ನಡ",
        "english_name": "Kannada",
        "code": "kn",
        "speech_code": "kn-IN",
        "flag": "🇮🇳",
        
        "praise": [
            "ಸರಿಯಾಗಿ ಹೇಳಿದ್ದೀರಿ! 👏",
            "ಅದ್ಭುತ! 🌟",
            "ಚೆನ್ನಾಗಿದೆ! 😊",
            "ಒಳ್ಳೆಯದು! 👍",
            "ಸೂಪರ್! ⭐"
        ],
        
        "encouragement": [
            "ಒಳ್ಳೆಯ ಪ್ರಯತ್ನ 🙂",
            "ಚೆನ್ನಾಗಿ ಪ್ರಯತ್ನಿಸಿದ್ದೀರಿ 💪",
            "ಇನ್ನೂ ಚೆನ್ನಾಗಿ ಬರುತ್ತದೆ 🌈",
            "ಪ್ರಯತ್ನ ಮುಂದುವರಿಸಿ 🎯"
        ],
        
        "ui": {
            "welcome": "ನಮಸ್ಕಾರ! 🙏",
            "teacher_intro": "ನಾನು ನಿಮ್ಮ ಕನ್ನಡ teacher! 👨‍🏫",
            "click_to_speak": "ಮೈಕ್ ಅನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಮಾತನಾಡಲು ಪ್ರಾರಂಭಿಸಿ",
            "listening": "ಕೇಳುತ್ತಿದ್ದೇನೆ...",
            "speaking": "Teacher ಮಾತನಾಡುತ್ತಿದ್ದಾರೆ...",
            "click_mic": "ಮಾತನಾಡಲು ಕ್ಲಿಕ್ ಮಾಡಿ",
            "full_sentence": "ಪೂರ್ಣ ವಾಕ್ಯ ಹೇಳಿ 🙂",
            "repeat_now": "ಈಗ ನೀವು ಹೇಳಿ.",
            "correct_sentence": "ಸರಿಯಾದ ವಾಕ್ಯ:",
            "corrections": "ತಿದ್ದುಪಡಿಗಳು:",
            "your_progress": "ನಿಮ್ಮ ಪ್ರಗತಿ 📊",
            "total_conversations": "ಒಟ್ಟು ಸಂಭಾಷಣೆಗಳು",
            "corrections_count": "ತಿದ್ದುಪಡಿಗಳು",
            "accuracy_percent": "ಸರಿಯಾದ ಶೇಕಡಾವಾರು"
        }
    },
    
    "bengali": {
        "name": "বাংলা",
        "english_name": "Bengali",
        "code": "bn",
        "speech_code": "bn-IN",
        "flag": "🇮🇳",
        
        "praise": [
            "একদম ঠিক বলেছ! 👏",
            "অসাধারণ! 🌟",
            "খুব ভালো! 😊",
            "দারুণ! 👍",
            "সুপার! ⭐"
        ],
        
        "encouragement": [
            "ভালো চেষ্টা 🙂",
            "খুব ভালো চেষ্টা করেছ 💪",
            "আরও ভালো হবে 🌈",
            "চেষ্টা চালিয়ে যাও 🎯"
        ],
        
        "ui": {
            "welcome": "নমস্কার! 🙏",
            "teacher_intro": "আমি তোমার বাংলা teacher! 👨‍🏫",
            "click_to_speak": "মাইক ক্লিক করে কথা বলা শুরু করো",
            "listening": "শুনছি...",
            "speaking": "Teacher বলছেন...",
            "click_mic": "বলার জন্য ক্লিক করো",
            "full_sentence": "পুরো বাক্য বলো 🙂",
            "repeat_now": "এখন তুমি বলো.",
            "correct_sentence": "সঠিক বাক্য:",
            "corrections": "সংশোধন:",
            "your_progress": "তোমার অগ্রগতি 📊",
            "total_conversations": "মোট কথোপকথন",
            "corrections_count": "সংশোধন",
            "accuracy_percent": "সঠিক শতাংশ"
        }
    }
}

def get_language_config(language_code: str):
    """Get configuration for a specific language"""
    return SUPPORTED_LANGUAGES.get(language_code, SUPPORTED_LANGUAGES["tamil"])

def get_available_languages():
    """Get list of all available languages"""
    return [
        {
            "code": code,
            "name": config["name"],
            "english_name": config["english_name"],
            "flag": config["flag"]
        }
        for code, config in SUPPORTED_LANGUAGES.items()
    ]
