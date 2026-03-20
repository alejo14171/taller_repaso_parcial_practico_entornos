# Gemini Chatbot con FastAPI

## Configuración

1. Crear un archivo `.env` en el proyecto con:

```
GEMINI_API_KEY=your_gemini_api_key
```

2. Crear y activar el entorno virtual:

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias:

```
pip install fastapi uvicorn python-dotenv google-genai
```

## Ejecución

```
uvicorn main:app --reload
```

Abrir `http://127.0.0.1:8000` en el navegador.

