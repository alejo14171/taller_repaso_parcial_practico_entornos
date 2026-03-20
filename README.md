# Documentación

Proyecto mínimo que muestra una integración entre FastAPI y Google Gemini (Generative AI).

Contenido
- `main.py`: servidor FastAPI que expone un endpoint `/chat` y sirve la interfaz en `/`.
- `static/index.html`: interfaz web (HTML/CSS/JS) para chatear con Gemini.
- `.env`: archivo local (no versionado) que contiene `GEMINI_API_KEY`.

Requisitos
- Python 3.10+ (se probó con 3.12)
- Un entorno virtual (recomendado)
- Dependencias en `requeriments.txt` o instálalas manualmente:

```bash
python -m pip install -r ../requirements.txt
# o desde fork_colab:
python -m pip install google-generativeai python-dotenv fastapi uvicorn
```

Configuración
1. Crea un archivo `.env` en la carpeta `fork_colab` con tu clave de API de Google Gemini:

```
GEMINI_API_KEY=TU_CLAVE_AQUI
```

2. **No** subas ni comitees el archivo `.env` — mantiene tu clave privada.

Ejecutar la aplicación (desarrollo)
```bash
cd fork_colab
# activar tu venv si corresponde
uvicorn main:app --reload
# o usar fastapi dev
fastapi dev main.py
```

Uso
- Abre `http://127.0.0.1:8000/` en tu navegador para ver la interfaz de chat.
- Endpoint backend principal:
	- `POST /chat` — cuerpo JSON `{ "message": "texto" }` devuelve `{ "response": "texto de Gemini" }`.
	- `GET /llm/{prompt}` — endpoint simple para llamadas ad-hoc (dev).

Notas importantes
- El servidor carga la variable `GEMINI_API_KEY` desde `.env` usando `python-dotenv`.
- Si recibes errores 429 `RESOURCE_EXHAUSTED`, tu proyecto/clave no tiene cuota para el modelo solicitado. Soluciones:
	- Habilitar/actualizar facturación en Google Cloud / AI Studio.
	- Usar otra clave/proyecto con cuota suficiente.
	- Usar un modelo al que tengas acceso.
- El código ya intenta devolver mensajes de error claros al frontend; considera añadir reintentos exponenciales o cachear respuestas para reducir uso.

Seguridad y despliegue
- Ajusta `CORS` para producción (actualmente `allow_origins` está en `*`).
- No expongas la clave en repositorios públicos ni en el frontend.

Contacto
Si necesitas que añada tests, fije versiones exactas en `requeriments.txt` o prepare despliegue, dime y lo hago.

