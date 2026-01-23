import React from 'react';

/**
 * Progress Tracker Component
 * Displays student statistics and encouragement
 */
const ProgressTracker = ({ stats, isLoading }) => {
    if (!stats || isLoading) {
        return null;
    }

    const { improvement_rate, total_corrections, conversation_length } = stats;

    // Progress bar color based on improvement rate
    const getProgressColor = (rate) => {
        if (rate >= 80) return '#4ade80'; // Green
        if (rate >= 60) return '#fbbf24'; // Yellow
        return '#f87171'; // Red
    };

    return (
        <div className="progress-tracker">
            <h3>உன் முன்னேற்றம் 📊</h3>

            <div className="stats-grid">
                <div className="stat-card">
                    <div className="stat-value">{conversation_length}</div>
                    <div className="stat-label">மொத்த உரையாடல்கள்</div>
                </div>

                <div className="stat-card">
                    <div className="stat-value">{total_corrections}</div>
                    <div className="stat-label">திருத்தங்கள்</div>
                </div>

                <div className="stat-card full-width">
                    <div className="stat-label">சரியான சதவீதம்</div>
                    <div className="progress-bar">
                        <div
                            className="progress-fill"
                            style={{
                                width: `${improvement_rate}%`,
                                backgroundColor: getProgressColor(improvement_rate)
                            }}
                        >
                            <span className="progress-text">{improvement_rate}%</span>
                        </div>
                    </div>
                </div>
            </div>

            {improvement_rate >= 80 && (
                <div className="achievement">
                    🌟 அருமை! மிக நன்றாக செய்கிறாய்!
                </div>
            )}

            {improvement_rate >= 60 && improvement_rate < 80 && (
                <div className="achievement">
                    👍 நல்லா வருது! தொடர்ந்து செய்!
                </div>
            )}
        </div>
    );
};

export default ProgressTracker;
