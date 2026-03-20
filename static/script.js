const chatWindow = document.getElementById('chatWindow');
const chatForm = document.getElementById('chatForm');
const promptInput = document.getElementById('promptInput');

function addMessage(text, role) {
  const message = document.createElement('article');
  message.className = `message ${role}`;
  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.textContent = text;
  message.appendChild(bubble);
  chatWindow.appendChild(message);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendPrompt(prompt) {
  const response = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'Error en la petición');
  }

  const result = await response.json();
  return result.answer;
}

chatForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const prompt = promptInput.value.trim();
  if (!prompt) return;

  addMessage(prompt, 'user');
  promptInput.value = '';
  promptInput.disabled = true;
  chatForm.querySelector('button').disabled = true;

  try {
    const answer = await sendPrompt(prompt);
    addMessage(answer, 'bot');
  } catch (err) {
    addMessage('Error: ' + err.message, 'bot');
  } finally {
    promptInput.disabled = false;
    chatForm.querySelector('button').disabled = false;
    promptInput.focus();
  }
});
