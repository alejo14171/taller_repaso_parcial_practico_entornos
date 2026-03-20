from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import chat

app = FastAPI(title="FastAPI + Gemini Example")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "message": "API funcionando"}


app.include_router(chat.router, prefix="/chat", tags=["chat"])