import os
from dotenv import load_dotenv
from fastapi import FastAPI
from google import genai
from pydantic import BaseModel



load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")

print("API KEY:", API_KEY)  # DEBUG

os.environ["GEMINI_API_KEY"] = API_KEY

client = genai.Client()

class Mensaje(BaseModel):
    texto: str

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.post("/chat")
def chat(mensaje: Mensaje):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=mensaje.texto
        )
        return {
            "respuesta": response.text
        }
    except Exception as e:
        return {"error": str(e)}
    
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
