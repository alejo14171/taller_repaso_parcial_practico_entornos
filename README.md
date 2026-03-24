# Chatbot Moderno - FastAPI + Gemini + Frontend

Un chatbot moderno con backend en FastAPI integrado con Google Gemini y frontend elegante en HTML/CSS/JavaScript puro.

## Estructura del Proyecto

```
/
├── backend/
│   ├── src/
│   │   ├── main.py              # API FastAPI
│   │   ├── services/
│   │   │   └── gemini_service.py # Servicio de integración con Gemini
│   │   └── schemas/
│   │       └── chat_schema.py    # Esquemas Pydantic
│   └── requirements.txt          # Dependencias Python
├── frontend/                     # Frontend anterior (archivos separados)
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md                     # Este archivo
```

## Backend - FastAPI

### Instalación

```bash
cd backend
pip install -r requirements.txt
```

### Ejecutar el servidor

```bash
cd backend/src
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Endpoints

- `POST /chat` - Envía un mensaje al chatbot
  - Body: `{"message": "Hola"}`
  - Response: `{"response": "¡Hola! ¿En qué puedo ayudarte?"}`

- `GET /` - Verifica que la API esté funcionando

## Frontend

### Uso

1. Abre `index.html` en tu navegador (desde la raíz del proyecto)
2. Escribe un mensaje en el campo de texto
3. Presiona Enter o haz clic en "Enviar"
4. El chatbot responderá automáticamente

### Características

- ✅ **Diseño moderno** con gradientes azules y efecto burbujas
- ✅ **Glassmorphism** con contenedor transparente y blur
- ✅ **Responsive** y centrado en pantalla
- ✅ Mensajes diferenciados (usuario/bot) con burbujas
- ✅ Animaciones suaves al aparecer mensajes y hover
- ✅ Indicador de "escribiendo..." con puntos animados
- ✅ Scroll automático hacia el último mensaje
- ✅ Manejo de errores y validaciones
- ✅ Conexión con backend FastAPI
- ✅ Auto-resize del campo de entrada
- ✅ Soporte para Shift+Enter (nueva línea)

## Tecnologías

- **Backend**: FastAPI, Pydantic, Uvicorn, Google Gemini AI
- **Frontend**: HTML5, CSS3 (Gradientes, Animaciones, Glassmorphism), JavaScript (Vanilla)
- **Comunicación**: REST API con JSON

## Cómo funciona

1. El usuario escribe un mensaje en el frontend
2. Se envía una petición POST al backend (`/chat`)
3. El backend procesa el mensaje usando `gemini_service.py`
4. Se retorna una respuesta simulada
5. El frontend muestra la respuesta del bot

## Desarrollo

### Ejecutar ambos servicios

1. **Terminal 1 - Backend:**
   ```bash
   cd backend/src
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Terminal 2 - Frontend:**
   - Abre `frontend/index.html` en tu navegador
   - O usa un servidor local: `python -m http.server 3000`

### Testing

Puedes probar la API directamente:

```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hola"}'
```

## Personalización

- **Respuestas del bot**: Edita `backend/src/services/gemini_service.py`
- **Estilos**: Modifica `frontend/styles.css`
- **Funcionalidad**: Actualiza `frontend/script.js`

¡Listo para usar! 🚀
