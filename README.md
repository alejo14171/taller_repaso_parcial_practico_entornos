# Chat IA — Proyecto Demo

Pequeña aplicación de ejemplo con arquitectura limpia: backend en FastAPI y frontend estático (HTML/CSS/JS puro).

Descripción rápida
- Backend: API REST que expone `POST /chat` y devuelve respuestas generadas (simuladas o mediante un proveedor de IA).
- Frontend: interfaz de chat moderna con burbujas, experiencia responsiva y animaciones.

Estructura del proyecto

- backend/
	- main.py — arranque de FastAPI y configuración CORS ([backend/main.py](backend/main.py))
	- routes/chat.py — ruta `POST /chat` ([backend/routes/chat.py](backend/routes/chat.py))
	- schemas/chat.py — modelos Pydantic de request/response ([backend/schemas/chat.py](backend/schemas/chat.py))
	- services/ai_service.py — servicio IA (simulado por defecto, opción de integrar Gemini) ([backend/services/ai_service.py](backend/services/ai_service.py))

- frontend/
	- index.html — interfaz principal ([frontend/index.html](frontend/index.html))
	- styles.css — estilos modernos y modo oscuro ([frontend/styles.css](frontend/styles.css))
	- app.js — lógica de UI e integración con la API ([frontend/app.js](frontend/app.js))

Dependencias
- Python y dependencias listadas en `requirements.txt`.

Variables de entorno
- `GEMINI_API_KEY` — (opcional) clave para usar la API de Gemini. Si no existe, el backend usa el modo simulado (devuelve el mensaje invertido).
- `GEMINI_API_URL` — (opcional) URL del endpoint de generación si necesitas cambiarla.

Ejecución local (desarrollo)

1. Crear/activar entorno virtual e instalar dependencias:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Iniciar el backend (uvicorn):

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

3. Servir el frontend (estático) desde la carpeta `frontend` (opción rápida):

```bash
python -m http.server 5500 --directory frontend
# Abrir http://localhost:5500/index.html
```

Uso de la API
- Endpoint: `POST /chat` (JSON)

Request example:

```json
{ "message": "Hola, ¿qué tal?" }
```

Response example:

```json
{ "response": "IA dice: " }
```

Notas de implementación
- Se usa Pydantic para validar `message` (no vacío).
- Se maneja error 400 para input vacío y 500 para errores internos.
- CORS habilitado para desarrollo local.
- `backend/services/ai_service.py` contiene la lógica para usar Gemini si `GEMINI_API_KEY` está configurada; de lo contrario vuelve el modo simulado.

Próximos pasos sugeridos
- Integrar y probar con la API real de Gemini (proporcionar formato de petición/URL).
- Añadir pruebas unitarias y CI.
- Mejorar persistencia de conversación si se desea histórico.


