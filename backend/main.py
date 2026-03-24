import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.schemas.chat_schema import ChatRequest
from src.services.gemini_service import get_chat_response
from dotenv import load_dotenv

load_dotenv()

# Crear la aplicación FastAPI
app = FastAPI(
    title="Chatbot API",
    description="API simple para chatbot",
    version="1.0.0"
)

# Configurar CORS para permitir todas las conexiones
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las origines
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los headers
)


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    print("Iniciando chat")
    try:
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")

        result = await get_chat_response(request.message.strip())

        if not result["success"]:
            raise HTTPException(
                status_code=502,
                detail=f"Error con Gemini: {result['error']}"
            )

        return {
            "response": result["data"]
        }

    except HTTPException:
        # Re-lanzar excepciones HTTP
        raise
    except Exception as e:
        # Manejo genérico de errores
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


@app.get("/status")
async def status():
    return {
        "api_status": "running",
        "gemini_configured": bool(os.getenv("GEMINI_API_KEY"))
    }
