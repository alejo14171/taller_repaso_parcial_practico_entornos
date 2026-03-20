// Elementos del DOM
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chatMessages');
const loadingIndicator = document.getElementById('loadingIndicator');

// Event listeners
sendButton.addEventListener('click', handleSendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSendMessage();
    }
});

/**
 * Maneja el envío de mensajes
 */
async function handleSendMessage() {
    const userMessage = messageInput.value.trim();

    // Validación: no enviar mensajes vacíos
    if (!userMessage) {
        return;
    }

    // Deshabilitar input y botón mientras se procesa
    messageInput.disabled = true;
    sendButton.disabled = true;
    loadingIndicator.style.display = 'block';

    // Mostrar mensaje del usuario en el chat
    addMessageToChat(userMessage, 'user');

    // Limpiar input
    messageInput.value = '';

    try {
        // Realizar petición fetch al backend
        const response = await fetch(`/llm/${encodeURIComponent(userMessage)}`);

        // Verificar si la respuesta fue exitosa
        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }

        // Parsear respuesta JSON
        const data = await response.json();

        // Mostrar respuesta del bot
        addMessageToChat(data.Respuesta, 'bot');
    } catch (error) {
        console.error('Error al enviar el mensaje:', error);
        addMessageToChat(
            '❌ Error: No pude procesar tu solicitud. Intenta de nuevo más tarde.',
            'bot'
        );
    } finally {
        // Re-habilitar input y botón
        messageInput.disabled = false;
        sendButton.disabled = false;
        loadingIndicator.style.display = 'none';
        messageInput.focus();
    }
}

/**
 * Agrega un mensaje al chat
 * @param {string} message - Contenido del mensaje
 * @param {string} sender - 'user' o 'bot'
 */
function addMessageToChat(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    const messageP = document.createElement('p');
    messageP.textContent = message;

    messageDiv.appendChild(messageP);
    chatMessages.appendChild(messageDiv);

    // Auto-scroll al último mensaje
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
