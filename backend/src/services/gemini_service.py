import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró la API KEY de Gemini")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3-flash-preview")

async def get_chat_response(message: str):
    print("Mensaje recibido en Gemini_service")

    try:
        response = model.generate_content(message)

        print("Respuesta completa:", response)

        if not response or not hasattr(response, "text"):
            return {
                "success": False,
                "error": "Respuesta inválida de Gemini"
            }

        return {
            "success": True,
            "data": response.text
        }

    except Exception as e:
        print("Error Gemini:", e)
        return {
            "success": False,
            "error": str(e)
        }

