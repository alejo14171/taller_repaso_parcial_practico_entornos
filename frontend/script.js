// Configuración del chatbot frontend
const API_URL = 'http://localhost:8000/chat';

// Elementos del DOM
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chatMessages');

// Estado de la aplicación
let isLoading = false;

/**
 * Agrega un mensaje al área de chat
 * @param {string} text - El texto del mensaje
 * @param {string} sender - 'user' o 'bot'
 */
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.textContent = text;

    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

/**
 * Hace scroll automático hacia el último mensaje
 */
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Limpia el campo de entrada
 */
function clearInput() {
    messageInput.value = '';
}

/**
 * Habilita o deshabilita los controles de entrada
 * @param {boolean} enable - true para habilitar, false para deshabilitar
 */
function setInputEnabled(enable) {
    messageInput.disabled = !enable;
    sendButton.disabled = !enable;
    isLoading = !enable;
}

/**
 * Envía un mensaje al servidor
 * @param {string} message - El mensaje a enviar
 */
async function sendMessage(message) {
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message
            })
        });

        console.log(message)

        if (!response.ok) {
            throw new Error(`Error del servidor: ${response.status}`);
        }

        const data = await response.json();
        return data.response;

    } catch (error) {
        console.error('Error al enviar mensaje:', error);
        return `Error: ${error.message}`;
    }
}

/**
 * Maneja el envío de un mensaje
 */
async function handleSendMessage() {
    const message = messageInput.value.trim();

    // Validar que no esté vacío
    if (!message) {
        return;
    }

    // Evitar envíos múltiples
    if (isLoading) {
        return;
    }

    // Mostrar mensaje del usuario
    addMessage(message, 'user');
    clearInput();
    setInputEnabled(false);

    // Enviar al servidor y mostrar respuesta
    const response = await sendMessage(message);
    addMessage(response, 'bot');

    // Re-habilitar controles
    setInputEnabled(true);
}

// Event listeners
sendButton.addEventListener('click', handleSendMessage);

messageInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        handleSendMessage();
    }
});

// Inicializar el chat con un mensaje de bienvenida
window.addEventListener('load', () => {
    addMessage('¡Hola! Soy un chatbot simple. ¿En qué puedo ayudarte?', 'bot');
    messageInput.focus();
});
