import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from google import genai
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la API key (se validará cuando se use)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Crear instancia de FastAPI
app = FastAPI(title="Chat IA - Asistente Simple")

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    """
    Sirve el archivo index.html en la ruta raíz.
    Esto permite acceder a la interfaz del chat en http://localhost:8000/
    """
    return FileResponse("static/index.html", media_type="text/html")


@app.get("/llm/{prompt}")
async def chat_with_llm(prompt: str):
    """
    Endpoint que procesa el mensaje del usuario y responde con Gemini.

    Args:
        prompt (str): El mensaje del usuario codificado en la URL

    Returns:
        dict: Respuesta generada por Gemini en formato JSON
    """
    try:
        # Validar que la API key esté configurada
        if not GEMINI_API_KEY:
            return {
                "Respuesta": "❌ Error: GEMINI_API_KEY no configurada. "
                "Por favor, configura tu API key en el archivo .env"
            }
        
        # Crear cliente con la API key
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # Generar respuesta con Gemini
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

        # Obtener el texto de la respuesta
        response_text = response.text if response.text else "No se pudo generar una respuesta."

        return {"Respuesta": response_text}

    except Exception as e:
        # Manejo de errores
        error_message = (
            f"Error al procesar la solicitud: {str(e)}. "
            "Por favor, intenta de nuevo más tarde."
        )
        return {"Respuesta": error_message}