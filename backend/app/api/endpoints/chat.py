from fastapi import APIRouter

router = APIRouter()

@router.options("/chat/")
async def chat_options():
    return {"status": "OK"}

@router.post("/chat/")
async def chat(request: ChatRequest):
    # Aquí va la lógica de tu función de chat
    return {"response": "Respuesta del chatbot"}
