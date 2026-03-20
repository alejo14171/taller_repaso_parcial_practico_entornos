import os

from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from google import genai


load_dotenv()

GEMINI_MODEL = "gemini-2.5-flash"
# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    global gemini_client
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY no está configurado. Agrégalo a tu archivo .env"
        )
    gemini_client = genai.Client(api_key=api_key)
    yield


app = FastAPI(title="Gemini Chat API", description="FastAPI + Google Gemini", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

gemini_client: genai.Client | None = None


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/")
async def homepage():
    return FileResponse("static/index.html")


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest) -> ChatResponse:
    if gemini_client is None:
        raise HTTPException(status_code=503, detail="Cliente Gemini no inicializado")
    try:
        resp = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=req.message,
        )
    except Exception as exc:
        status = 429 if "429" in str(exc) else 502
        raise HTTPException(status_code=status, detail=f"Error con Gemini API: {exc}")

    return ChatResponse(response=resp.text or "")


@app.post("/llm", response_model=dict)
async def llm_endpoint(req: ChatRequest):
    if gemini_client is None:
        raise HTTPException(status_code=503, detail="Cliente Gemini no inicializado")
    try:
        resp = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=req.message,  
        )
    except Exception as exc:
        status = 429 if "429" in str(exc) else 502
        raise HTTPException(status_code=status, detail=f"Error con Gemini API: {exc}")

    return {"Respuesta": resp.text}