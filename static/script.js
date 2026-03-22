const messagesEl = document.getElementById('messages');
const form = document.getElementById('chatForm');
const input = document.getElementById('messageInput');

function addMessage(text, cls = 'bot'){
  const div = document.createElement('div');
  div.className = `bubble ${cls}`;
  div.textContent = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

form.addEventListener('submit', async (e) =>{
  e.preventDefault();
  const text = input.value && input.value.trim();
  if(!text) return;
  addMessage(text, 'user');
  input.value = '';

  try{
    const res = await fetch('/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: text})
    });

    if(!res.ok){
      const err = await res.json().catch(()=>({detail:res.statusText}));
      addMessage('Error: ' + (err.detail || res.statusText), 'bot');
      return;
    }

    const data = await res.json();
    addMessage(data.response || '(sin respuesta)', 'bot');
  }catch(err){
    addMessage('Error de conexión: ' + err.message, 'bot');
  }
});
