from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()

# Lee la API KEY desde la variable de entorno `GEMINI_API_KEY`
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

app = FastAPI(title="Gemini Flash Chat - Backend")

# Habilitar CORS (ajustar `allow_origins` en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


def call_gemini(prompt: str, api_key: str) -> str:
    from google import genai

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text


@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    """Endpoint que recibe { message: string } y devuelve { response: string }."""
    api_key = GEMINI_API_KEY or os.getenv("GEMINI_API_KEY")
    if not api_key:
        return JSONResponse(
            status_code=500,
            content={"error": "GEMINI_API_KEY no está configurada. Consulte .env.example"},
        )

    try:
        # Llamada a la función separada que consulta al modelo
        text = call_gemini(req.message, api_key)
        return {"response": text}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/health")
def health_check():
    """Endpoint de salud simple."""
    return {"status": "ok"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}