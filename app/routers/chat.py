from fastapi import APIRouter, HTTPException, status
from ..models.schemas import ChatRequest, ChatResponse
from ..services.gemini_service import generate_text, GeminiServiceError

router = APIRouter()


@router.post("", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    try:
        reply = generate_text(payload.message)
    except GeminiServiceError as e:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(e))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor",
        )
    return ChatResponse(reply=reply)
