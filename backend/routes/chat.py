from fastapi import APIRouter, HTTPException
import logging

from backend.schemas.chat import ChatRequest, ChatResponse
from backend.services.ai_service import generate_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
    msg = payload.message.strip()
    if not msg:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")
    try:
        response_text = await generate_response(msg)
        return ChatResponse(response=response_text)
    except Exception as e:
        logging.exception("Error handling /chat request")
        # For debugging return the underlying error message in detail (can be changed to a generic message)
        raise HTTPException(status_code=500, detail=str(e))
