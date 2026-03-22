# Chat básico con Gemini 3 Flash Preview

Este repositorio contiene un ejemplo minimalista fullstack que conecta un frontend estático (HTML/CSS/JS puro) con un backend en Python (FastAPI). El backend actúa como proxy hacia el modelo Gemini (Google Generative AI) y expone un endpoint `POST /chat` que el frontend consume mediante `fetch`.

Contenido principal

- [main.py](main.py): servidor FastAPI y función que llama al modelo Gemini.
- [static/index.html](static/index.html): interfaz web simple (chat).
- [static/styles.css](static/styles.css): estilos del chat.
- [static/script.js](static/script.js): lógica cliente (envía mensajes a `POST /chat`).
- [.env.example](.env.example): ejemplo de variables de entorno.
- [requirements.txt](requirements.txt): dependencias Python.

Estructura del proyecto

```
.
├─ main.py
├─ requirements.txt
├─ .env.example
└─ static/
	 ├─ index.html
	 ├─ styles.css
	 └─ script.js
```

Instalación y ejecución

1. Crear un entorno virtual (recomendado) e instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configurar la API key: copia `.env.example` a `.env` y añade tu clave:

```bash
cp .env.example .env
# editar .env y poner:
# GOOGLE_API_KEY=tu_api_key_aqui
```

3. Ejecutar el servidor de desarrollo con `uvicorn`:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. Abrir el frontend en el navegador: `http://localhost:8000/`

Descripción del backend

El backend está en [main.py](main.py). Sus responsabilidades principales son:

- Cargar variables de entorno (usa `python-dotenv`).
- Configurar CORS para permitir conexiones desde el frontend estático.
- Servir los archivos estáticos desde la carpeta `static/`.
- Exponer el endpoint `POST /chat` que espera un JSON: `{ "message": "texto del usuario" }`.
- Llamar al cliente oficial de Google Generative AI (`google.generativeai`) para obtener la respuesta del modelo.

Endpoint `/chat`

- Método: `POST`
- Ruta: `/chat`
- Payload (JSON):

```json
{ "message": "Hola, ¿cómo estás?" }
```

- Respuesta (JSON):

```json
{ "response": "Respuesta generada por Gemini..." }
```

Errores comunes y códigos HTTP

- 400 Bad Request: payload inválido o falta el campo `message`.
- 500 Internal Server Error: problema de configuración (por ejemplo, `GOOGLE_API_KEY` no establecido) o la librería cliente no instalada.

Notas sobre la integración con Gemini

- El proyecto intenta usar la librería `google.generativeai` (indicada en `requirements.txt`). Dependiendo de la versión de la librería y del entorno, la API del cliente puede variar; `main.py` incluye manejo flexible de formas de respuesta comunes.
- Variable de entorno importante:

```
GOOGLE_API_KEY=tu_api_key_aqui
GEMINI_MODEL=gemini-3-flash-preview  # opcional
```

- Si prefieres instalar otra librería o versión (por ejemplo, `google-genai`), modifica `requirements.txt` y la llamada en `main.py` según la documentación del cliente que uses.

Frontend

El frontend es deliberadamente simple y está en `static/`:

- [static/index.html](static/index.html): contiene la estructura del chat, un área para mensajes y un formulario con input y botón.
- [static/script.js](static/script.js): captura el evento `submit`, envía el mensaje a `/chat` con `fetch`, y agrega los mensajes al DOM.
- [static/styles.css](static/styles.css): estilos básicos, diferencia visual entre mensajes de usuario y del bot.

Ejemplo de uso (desde línea de comandos)

```bash
curl -X POST http://localhost:8000/chat \
	-H "Content-Type: application/json" \
	-d '{"message": "Dime un chiste corto"}'

# Respuesta esperada:
# { "response": "Aquí va un chiste corto..." }
```

Buenas prácticas y seguridad

- No subas tu archivo `.env` a sistemas de control de versiones. Añade `.env` a `.gitignore`.
- Limita el acceso a la API key y controla los costos del uso del modelo.
- Para producción, no uses `--reload` y considera ejecutar detrás de un proxy (nginx) y con gestión de procesos (systemd, gunicorn/uvicorn workers).

Depuración

- Si recibes un error indicando que `google.generativeai` no está instalado, instala la dependencia:

```bash
pip install google-generativeai
```

- Si el endpoint devuelve errores 500 con mensajes sobre la API key, verifica que `.env` tenga `GOOGLE_API_KEY` y que `main.py` pueda leerla (reinicia el servidor después de cambiar `.env`).

Extensiones y personalización

- Cambiar el modelo: ajustar `GEMINI_MODEL` en `.env`.
- Añadir autenticación al endpoint `/chat` si el servicio va a estar expuesto públicamente.

Contacto

Si quieres que te ayude a desplegar este ejemplo en un servidor o a añadir autenticación / registro de conversaciones, dímelo y lo preparo.

