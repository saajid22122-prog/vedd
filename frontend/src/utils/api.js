import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

/**
 * Fetch available languages
 */
export const fetchLanguages = async () => {
    try {
        const response = await api.get('/languages');
        return response.data.languages;
    } catch (error) {
        console.error('Languages Fetch Error:', error);
        return [];
    }
};

/**
 * Send student message to tutor and get response
 */
export const sendMessage = async (text, sessionId, language = 'tamil') => {
    try {
        const response = await api.post('/chat', {
            text,
            session_id: sessionId,
            language,
        });
        return response.data;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
};

/**
 * Get session statistics
 */
export const getSessionStats = async (sessionId, language = 'tamil') => {
    try {
        const response = await api.get(`/session/${sessionId}/stats`, {
            params: { language }
        });
        return response.data;
    } catch (error) {
        console.error('Stats Error:', error);
        throw error;
    }
};

/**
 * End session
 */
export const endSession = async (sessionId, language = 'tamil') => {
    try {
        await api.delete(`/session/${sessionId}`, {
            params: { language }
        });
    } catch (error) {
        console.error('End Session Error:', error);
    }
};

export default api;
