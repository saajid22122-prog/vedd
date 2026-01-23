import { useState, useEffect } from 'react';
import VoiceControls from './components/VoiceControls';
import ChatDisplay from './components/ChatDisplay';
import ProgressTracker from './components/ProgressTracker';
import LanguageSelector from './components/LanguageSelector';
import { useSpeechRecognition } from './hooks/useSpeechRecognition';
import { useSpeechSynthesis } from './hooks/useSpeechSynthesis';
import { sendMessage, getSessionStats, fetchLanguages } from './utils/api';

// Language code to speech code mapping
const SPEECH_CODES = {
    'tamil': 'ta-IN',
    'hindi': 'hi-IN',
    'telugu': 'te-IN',
    'malayalam': 'ml-IN',
    'kannada': 'kn-IN',
    'bengali': 'bn-IN'
};

function App() {
    // Language state
    const [selectedLanguage, setSelectedLanguage] = useState('tamil');
    const [availableLanguages, setAvailableLanguages] = useState([]);

    // Generate unique session ID
    const [sessionId] = useState(() => `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);

    // Conversation state
    const [messages, setMessages] = useState([]);
    const [stats, setStats] = useState(null);
    const [isProcessing, setIsProcessing] = useState(false);

    // Get speech code for selected language
    const speechCode = SPEECH_CODES[selectedLanguage] || 'ta-IN';

    // Speech recognition and synthesis with language support
    const {
        isListening,
        transcript,
        startListening,
        stopListening,
        isSupported: isRecognitionSupported
    } = useSpeechRecognition(speechCode);

    const {
        speak,
        isSpeaking
    } = useSpeechSynthesis();

    // Fetch available languages on mount
    useEffect(() => {
        const loadLanguages = async () => {
            const langs = await fetchLanguages();
            setAvailableLanguages(langs);
        };
        loadLanguages();
    }, []);

    // When transcript is received, send to backend
    useEffect(() => {
        if (transcript && !isProcessing) {
            handleStudentMessage(transcript);
        }
    }, [transcript]);

    const handleStudentMessage = async (text) => {
        setIsProcessing(true);

        try {
            // Send message to backend with selected language
            const response = await sendMessage(text, sessionId, selectedLanguage);

            // Add to conversation history
            const newMessage = {
                studentText: text,
                tutorText: response.text,
                correction: response.correction,
                encouragement: response.encouragement,
                shouldRepeat: response.should_repeat
            };

            setMessages(prev => [...prev, newMessage]);

            // Speak tutor's response in selected language
            speak(response.text, speechCode);

            // Update stats
            fetchStats();

        } catch (error) {
            console.error('Error processing message:', error);
            // Error message in the selected language would be better, but fallback to English
            speak('Sorry, there was an error. Please try again.', 'en-US');
        } finally {
            setIsProcessing(false);
        }
    };

    const fetchStats = async () => {
        try {
            const sessionStats = await getSessionStats(sessionId, selectedLanguage);
            setStats(sessionStats);
        } catch (error) {
            console.error('Error fetching stats:', error);
        }
    };

    const handleLanguageChange = (newLanguage) => {
        setSelectedLanguage(newLanguage);
        // Clear messages when switching languages for a fresh start
        setMessages([]);
        setStats(null);
    };

    return (
        <div className="app-container">
            <header className="app-header">
                <div className="header-content">
                    <div className="header-left">
                        <h1>AI Voice Tutor</h1>
                        <p className="subtitle">Learn Indian Languages</p>
                    </div>
                    <LanguageSelector
                        selectedLanguage={selectedLanguage}
                        onLanguageChange={handleLanguageChange}
                        availableLanguages={availableLanguages}
                    />
                </div>
            </header>

            <main className="app-main">
                <div className="chat-section">
                    <ChatDisplay messages={messages} />
                </div>

                <div className="controls-section">
                    <VoiceControls
                        isListening={isListening}
                        isSpeaking={isSpeaking}
                        onStartListening={startListening}
                        onStopListening={stopListening}
                        isSupported={isRecognitionSupported}
                    />
                </div>

                {messages.length > 0 && (
                    <div className="stats-section">
                        <ProgressTracker stats={stats} isLoading={!stats} />
                    </div>
                )}
            </main>

            <footer className="app-footer">
                <p>💡 Tip: Chrome browser works best for voice recognition</p>
            </footer>
        </div>
    );
}

export default App;
