const API = (window.API_URL || 'http://localhost:8001') + '/chat'

const messagesEl = document.getElementById('messages')
const form = document.getElementById('composer')
const input = document.getElementById('input')

function scrollToBottom(){
  messagesEl.scrollTop = messagesEl.scrollHeight
}

function makeBubble(text, who='bot'){
  const wrap = document.createElement('div')
  wrap.className = 'bubble ' + (who==='user' ? 'user' : 'bot')
  wrap.innerText = text
  return wrap
}

function makeTyping(){
  const b = document.createElement('div')
  b.className = 'bubble bot'
  const t = document.createElement('div')
  t.className = 'typing'
  t.innerHTML = '<span></span><span></span><span></span>'
  b.appendChild(t)
  return b
}

async function sendMessage(text){
  // show user message immediately
  const userBubble = makeBubble(text,'user')
  messagesEl.appendChild(userBubble)
  scrollToBottom()

  // add typing placeholder
  const typing = makeTyping()
  messagesEl.appendChild(typing)
  scrollToBottom()

  try{
    const res = await fetch(API, {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({message: text})
    })

    const data = await res.json()
    const botText = data?.response || (data?.detail || 'Sin respuesta')

    // replace typing with actual message
    messagesEl.removeChild(typing)
    const botBubble = makeBubble(botText,'bot')
    messagesEl.appendChild(botBubble)
    scrollToBottom()
  }catch(err){
    messagesEl.removeChild(typing)
    const errBubble = makeBubble('Error de conexión. Intenta de nuevo.','bot')
    messagesEl.appendChild(errBubble)
    scrollToBottom()
  }
}

form.addEventListener('submit', e =>{
  e.preventDefault()
  const text = input.value.trim()
  if(!text) return
  input.value = ''
  sendMessage(text)
})

// autosize textarea
input.addEventListener('input', ()=>{
  input.style.height = 'auto'
  input.style.height = (input.scrollHeight) + 'px'
  scrollToBottom()
})

// small keyboard shortcut
input.addEventListener('keydown', e=>{
  if(e.key === 'Enter' && !e.shiftKey){
    e.preventDefault()
    form.requestSubmit()
  }
})
