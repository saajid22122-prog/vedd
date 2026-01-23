import React, { useEffect, useRef } from 'react';

/**
 * Chat Display Component
 * Shows conversation history with student and tutor messages
 * Highlights corrections when present
 */
const ChatDisplay = ({ messages }) => {
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    if (messages.length === 0) {
        return (
            <div className="chat-display empty">
                <div className="welcome-message">
                    <h2>வணக்கம்! 🙏</h2>
                    <p>நான் உன் தமிழ் teacher! 👨‍🏫</p>
                    <p className="instruction">மைக்கை click செய்து பேச தொடங்கு</p>
                </div>
            </div>
        );
    }

    return (
        <div className="chat-display">
            {messages.map((msg, index) => (
                <div key={index} className="message-group">
                    {/* Student message */}
                    <div className="message student">
                        <div className="message-avatar">👦</div>
                        <div className="message-bubble">
                            <div className="message-text">{msg.studentText}</div>
                        </div>
                    </div>

                    {/* Tutor response */}
                    <div className="message tutor">
                        <div className="message-avatar">👨‍🏫</div>
                        <div className="message-bubble">
                            {msg.correction && !msg.correction.is_correct && (
                                <div className="correction-box">
                                    <div className="correction-label">✏️ திருத்தம்:</div>
                                    <div className="corrected-text">{msg.correction.corrected_sentence}</div>
                                    {msg.correction.explanation && (
                                        <div className="explanation">{msg.correction.explanation}</div>
                                    )}
                                </div>
                            )}
                            <div className="message-text" style={{ whiteSpace: 'pre-line' }}>
                                {msg.tutorText}
                            </div>
                            {msg.encouragement && (
                                <div className="encouragement">{msg.encouragement}</div>
                            )}
                        </div>
                    </div>
                </div>
            ))}
            <div ref={messagesEndRef} />
        </div>
    );
};

export default ChatDisplay;
