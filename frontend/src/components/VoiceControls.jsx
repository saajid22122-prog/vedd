import React from 'react';

/**
 * Voice Controls Component
 * Displays microphone button with visual feedback for listening state
 */
const VoiceControls = ({
    isListening,
    isSpeaking,
    onStartListening,
    onStopListening,
    isSupported
}) => {
    if (!isSupported) {
        return (
            <div className="voice-controls error">
                <p>⚠️ உங்கள் பிரவுசர் voice recognition ஐ ஆதரிக்கவில்லை</p>
                <p className="small">Please use Chrome browser for best experience</p>
            </div>
        );
    }

    return (
        <div className="voice-controls">
            <button
                className={`mic-button ${isListening ? 'listening' : ''} ${isSpeaking ? 'disabled' : ''}`}
                onClick={isListening ? onStopListening : onStartListening}
                disabled={isSpeaking}
                aria-label={isListening ? 'Stop listening' : 'Start listening'}
            >
                <div className="mic-icon">
                    {isListening ? (
                        <span className="pulse">🎤</span>
                    ) : (
                        <span>🎤</span>
                    )}
                </div>
                <div className="mic-text">
                    {isSpeaking ? 'Teacher பேசுகிறார்...' : isListening ? 'கேட்கிறேன்...' : 'பேச Click செய்'}
                </div>
            </button>

            {isListening && (
                <div className="listening-indicator">
                    <div className="wave"></div>
                    <div className="wave"></div>
                    <div className="wave"></div>
                </div>
            )}
        </div>
    );
};

export default VoiceControls;
