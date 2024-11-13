from fastapi import APIRouter

router = APIRouter()

@router.options("/chat/")
async def chat_options():
    return {"status": "OK"}

@router.post("/chat/")
async def chat(request: ChatRequest):
    # Lógica del chat
    return {"response": "Respuesta del chatbot"}
