import { useState, useEffect, useCallback } from 'react';

/**
 * Custom hook for Web Speech API - Speech Recognition
 * Converts speech to text with multi-language support
 */
export const useSpeechRecognition = (languageCode = 'ta-IN') => {
    const [isListening, setIsListening] = useState(false);
    const [transcript, setTranscript] = useState('');
    const [recognition, setRecognition] = useState(null);
    const [isSupported, setIsSupported] = useState(false);

    useEffect(() => {
        // Check if browser supports Web Speech API
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

        if (SpeechRecognition) {
            const recognitionInstance = new SpeechRecognition();

            // Configure for selected language
            recognitionInstance.lang = languageCode;
            recognitionInstance.continuous = false;
            recognitionInstance.interimResults = false;
            recognitionInstance.maxAlternatives = 1;

            recognitionInstance.onresult = (event) => {
                const spokenText = event.results[0][0].transcript;
                setTranscript(spokenText);
            };

            recognitionInstance.onerror = (event) => {
                console.error('Speech recognition error:', event.error);
                setIsListening(false);
            };

            recognitionInstance.onend = () => {
                setIsListening(false);
            };

            setRecognition(recognitionInstance);
            setIsSupported(true);
        } else {
            console.warn('Web Speech API not supported in this browser');
            setIsSupported(false);
        }
    }, [languageCode]); // Re-initialize when language changes

    const startListening = useCallback(() => {
        if (recognition && !isListening) {
            setTranscript('');
            recognition.start();
            setIsListening(true);
        }
    }, [recognition, isListening]);

    const stopListening = useCallback(() => {
        if (recognition && isListening) {
            recognition.stop();
        }
    }, [recognition, isListening]);

    return {
        isListening,
        transcript,
        startListening,
        stopListening,
        isSupported,
    };
};
