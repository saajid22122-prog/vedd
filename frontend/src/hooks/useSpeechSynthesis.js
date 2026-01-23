import { useState, useEffect, useCallback } from 'react';

/**
 * Custom hook for Web Speech API - Speech Synthesis
 * Converts text to speech with multi-language support
 */
export const useSpeechSynthesis = () => {
    const [isSpeaking, setIsSpeaking] = useState(false);
    const [voices, setVoices] = useState([]);
    const [isSupported, setIsSupported] = useState(false);

    useEffect(() => {
        if ('speechSynthesis' in window) {
            setIsSupported(true);

            const loadVoices = () => {
                const availableVoices = window.speechSynthesis.getVoices();
                setVoices(availableVoices);
            };

            loadVoices();
            window.speechSynthesis.onvoiceschanged = loadVoices;
        } else {
            console.warn('Speech Synthesis not supported in this browser');
            setIsSupported(false);
        }
    }, []);

    const speak = useCallback((text, languageCode = 'ta-IN', onEnd = null) => {
        if (!isSupported) {
            console.warn('Speech synthesis not available');
            return;
        }

        // Cancel any ongoing speech
        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);

        // Try to find voice for the specified language
        const langVoice = voices.find(voice =>
            voice.lang.startsWith(languageCode.split('-')[0]) || voice.lang === languageCode
        );

        if (langVoice) {
            utterance.voice = langVoice;
        }

        utterance.lang = languageCode;
        utterance.rate = 0.9; // Slightly slower for clarity
        utterance.pitch = 1.1; // Friendly tone
        utterance.volume = 1.0;

        utterance.onstart = () => setIsSpeaking(true);
        utterance.onend = () => {
            setIsSpeaking(false);
            if (onEnd) onEnd();
        };
        utterance.onerror = (event) => {
            console.error('Speech synthesis error:', event);
            setIsSpeaking(false);
        };

        window.speechSynthesis.speak(utterance);
    }, [voices, isSupported]);

    const stop = useCallback(() => {
        window.speechSynthesis.cancel();
        setIsSpeaking(false);
    }, []);

    return {
        speak,
        stop,
        isSpeaking,
        isSupported,
    };
};
