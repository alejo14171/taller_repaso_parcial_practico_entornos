# Gemini Chatbot con FastAPI

## Descripción

Aplicación web full-stack que ofrece un chatbot basado en el modelo Gemini (Google GenAI). 

- Backend: FastAPI
- Frontend: HTML + CSS + JavaScript

Funcionalidad principal:
- Usuario envía mensaje desde UI
- Backend recibe en `/chat`
- Backend consulta a `gemini-3-flash-preview` y retorna respuesta
- Frontend muestra la conversación con estilo de chat

## Estructura del proyecto

```
main.py
README.md
static/
  ├─ index.html
  ├─ styles.css
  └─ script.js
.env
```

## Requerimientos

- Python 3.11+ (o 3.10)
- Dependencias: `fastapi`, `uvicorn`, `python-dotenv`, `google-genai`

## Configuración

1. Crear `.env` en raíz:

```bash
GEMINI_API_KEY=tu_api_key_gemini
```

2. Crear y activar entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install fastapi uvicorn python-dotenv google-genai
```

## Ejecución

```bash
uvicorn main:app --reload
```

Abrir 

- `http://127.0.0.1:8000` (UI)
- `http://127.0.0.1:8000/docs` (AutoDocs Swagger)

## Endpoints

### `GET /`
Carga el `index.html` de la carpeta `static`.

### `POST /chat`
JSON body:

```json
{ "prompt": "Hola, ¿cómo estás?" }
```

Respuesta:

```json
{ "answer": "Hola! ..." }
```

### `GET /items/{item_id}`
Ejemplo de endpoint adicional para pruebas.

## Frontend

- `static/index.html`: Estructura de la UI
- `static/styles.css`: Estilos y layout
- `static/script.js`: Lógica de interacción, envía solicitud /chat y actualiza el chat

## Uso desde la terminal (ejemplo cURL)

```bash
curl -X POST http://127.0.0.1:8000/chat -H 'Content-Type: application/json' -d '{"prompt":"Hola"}'
```

## Buenas prácticas y ampliaciones

- Añadir validaciones y límites de tamaño en prompts.
- Historial de chat en base de datos (SQLite / PostgreSQL).
- Autenticación de usuarios.
- Manejo de errores de red y reintentos.


