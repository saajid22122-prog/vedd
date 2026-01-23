import React, { useState, useEffect } from 'react';

/**
 * Language Selector Component
 * Allows users to select their preferred learning language
 */
const LanguageSelector = ({ selectedLanguage, onLanguageChange, availableLanguages }) => {
    const [isOpen, setIsOpen] = useState(false);

    if (!availableLanguages || availableLanguages.length === 0) {
        return null;
    }

    const currentLang = availableLanguages.find(lang => lang.code === selectedLanguage);

    return (
        <div className="language-selector">
            <button
                className="language-button"
                onClick={() => setIsOpen(!isOpen)}
                aria-label="Select language"
            >
                <span className="language-flag">{currentLang?.flag}</span>
                <span className="language-name">{currentLang?.name}</span>
                <span className="dropdown-arrow">{isOpen ? '▲' : '▼'}</span>
            </button>

            {isOpen && (
                <div className="language-dropdown">
                    {availableLanguages.map((lang) => (
                        <button
                            key={lang.code}
                            className={`language-option ${lang.code === selectedLanguage ? 'selected' : ''}`}
                            onClick={() => {
                                onLanguageChange(lang.code);
                                setIsOpen(false);
                            }}
                        >
                            <span className="language-flag">{lang.flag}</span>
                            <div className="language-info">
                                <span className="language-name">{lang.name}</span>
                                <span className="language-english">{lang.english_name}</span>
                            </div>
                            {lang.code === selectedLanguage && (
                                <span className="selected-check">✓</span>
                            )}
                        </button>
                    ))}
                </div>
            )}
        </div>
    );
};

export default LanguageSelector;
