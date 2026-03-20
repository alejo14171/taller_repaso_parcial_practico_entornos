# Documentación:

Proyecto de ejemplo: backend en Python con FastAPI integrado con Google Gemini (Generative Language API).

Estructura creada:

- app/
	- main.py
	- routers/chat.py
	- services/gemini_service.py
	- models/schemas.py
	- config/settings.py

Archivos añadidos:

- requirements.txt
- .env.example

Instrucciones rápidas:

1. Copia `.env.example` a `.env` y añade `GEMINI_API_KEY` con tu clave.

2. Instala dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación en modo desarrollo:

```bash
uvicorn app.main:app --reload
```

4. Endpoints:

- `GET /` — verificación del servicio.
- `POST /chat` — recibe JSON `{ "message": "..." }` y devuelve `{ "reply": "..." }`.

Notas:

- No incluyas claves reales en el repositorio. Usa `.env` y `.env.example` como plantilla.
- El servicio `gemini_service` usa una llamada HTTP a la API de Generative Language. Ajusta el `GEMINI_MODEL` y el manejo de respuesta según la versión de la API que uses.

