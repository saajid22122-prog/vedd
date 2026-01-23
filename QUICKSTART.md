# 🎤 AI Voice Tutor - Quick Start Guide

## ✅ Application is Running!

Both servers are now live:
- **Backend API:** http://localhost:8000
- **Frontend App:** http://localhost:5173

![AI Voice Tutor Interface](/Users/user/.gemini/antigravity/brain/7cec0958-1acc-4549-89cc-6aef57fddc11/ai_voice_tutor_welcome_screen_1769188160906.png)

---

## 🚀 How to Use

### 1. Open the App
The app should already be open in your browser at **http://localhost:5173**

If not, simply click: [Open AI Voice Tutor](http://localhost:5173)

### 2. Allow Microphone Access
When you click the microphone button, your browser will ask for microphone permission.
- Click **"Allow"** to enable voice input

### 3. Start Speaking in Tamil
1. **Click the microphone button** (the large 🎤 button)
2. **Wait for the listening indicator** (sound waves appear)
3. **Speak in Tamil** - try saying: "நான் பள்ளிக்கு போனேன்" (I went to school)
4. The app will:
   - Convert your speech to text
   - Analyze for grammar mistakes
   - Respond with feedback (correct or correction)
   - Speak the response back to you in Tamil

### 4. See Your Progress
After a few conversations, scroll down to see:
- Total conversations
- Number of corrections
- Accuracy percentage
- Achievement badges

---

## 📝 Example Conversations

### Correct Sentence
**You say:** "நான் பள்ளிக்கு போனேன்"  
**Tutor says:** "சரியாக சொன்னாய்! 👏 பள்ளியில் இன்று என்ன செய்தாய்?"

### Incorrect Sentence (Mixed Language)
**You say:** "நான் school போனேன்"  
**Tutor says:**  
```
நல்ல முயற்சி 🙂
சரியான வாக்கியம்: நான் பள்ளிக்கு போனேன்
'க்கு' இடத்தை குறிக்க பயன்படும்
இப்போ நீ சொல்லு.
```

### Short Answer
**You say:** "நல்லா"  
**Tutor says:** "முழு வாக்கியமாக சொல்லு 🙂"

---

## 🎯 Features to Try

✅ **Natural Conversation** - The tutor asks follow-up questions  
✅ **Grammar Correction** - See corrections highlighted in chat  
✅ **Voice Feedback** - Hear Tamil responses  
✅ **Progress Tracking** - Watch your stats improve  
✅ **Encouragement** - Get positive reinforcement  

---

## ⚙️ Backend API Endpoints

The backend is running on port 8000. You can test it:

### Health Check
```bash
curl http://localhost:8000
```

### Send Message
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "text": "நான் பள்ளிக்கு போனேன்",
    "session_id": "test123"
  }'
```

### Get Stats
```bash
curl http://localhost:8000/session/test123/stats
```

---

## 🔧 Stopping the Servers

When you're done:

**Backend:** Press `Ctrl+C` in the terminal running the backend  
**Frontend:** Press `Ctrl+C` in the terminal running the frontend

---

## 🎨 UI Features

- **Gradient Background** - Beautiful purple/blue gradient
- **Glassmorphism Cards** - Modern frosted glass effect
- **Pulsating Mic** - Animated when listening
- **Sound Waves** - Visual feedback during speech recognition
- **Color-Coded Messages** - Blue for student, gray for tutor
- **Highlighted Corrections** - Red border with green corrected text
- **Achievement Badges** - 🌟 for >80% accuracy, 👍 for 60-80%

---

## 📱 Browser Recommendation

**Best:** Chrome (full Tamil support)  
**Good:** Microsoft Edge  
**Limited:** Firefox, Safari

---

## 🆘 Troubleshooting

**Mic not working?**
- Check browser permissions
- Make sure you're on http://localhost (required for Web Speech API)

**Tamil not recognized?**
- Use Chrome browser
- Speak clearly and naturally
- Check system microphone is working

**Backend errors?**
- Check Groq API key in `backend/.env`
- Verify backend server is running on port 8000

---

## 🎉 Enjoy Learning Tamil!

The AI Voice Tutor is ready to help you improve your Tamil speaking skills through natural conversation!
