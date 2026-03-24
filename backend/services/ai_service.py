import os
import asyncio
import logging
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


async def generate_response(message: str) -> str:
    if not GEMINI_API_KEY:
        await asyncio.sleep(0.9)
        return f"IA dice: {message[::-1]}"

    try:
        from google import genai
    except Exception as e:
        raise RuntimeError(f"google.genai no está disponible: {e}")

    try:
        client = genai.Client()
    except Exception as e:
        raise RuntimeError(f"No se pudo inicializar genai.Client(): {e}")

    loop = asyncio.get_running_loop()

    def call_genai():
        return client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=message,
        )

    try:
        response = await loop.run_in_executor(None, call_genai)
    except Exception as e:
        raise RuntimeError(f"Error usando google.genai: {e}")

    try:
        if hasattr(response, "text"):
            return response.text
        if hasattr(response, "content"):
            return response.content

        try:
            data = response.to_dict()
        except Exception:
            data = None

        if isinstance(data, dict):
            if data.get("candidates"):
                c = data["candidates"][0]
                if isinstance(c, dict):
                    return c.get("content") or c.get("text") or str(c)
            if data.get("output") and isinstance(data.get("output"), list) and data.get("output"):
                first = data["output"][0]
                if isinstance(first, dict):
                    return first.get("content") or first.get("text") or str(first)
            if data.get("content"):
                return data.get("content")

        return str(response)
    except Exception as e:
        raise RuntimeError(f"No se pudo extraer la respuesta del cliente genai: {e}")
