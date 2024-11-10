from fastapi import APIRouter, HTTPException
from app.models.chat_request import ChatRequest
from app.core.utils import (
    generate_id, get_embedding, purge_old_data,
    initialize_openai_and_pinecone
)
import openai

router = APIRouter()

# Inicialización de servicios de OpenAI y Pinecone
openai_api_key, pinecone_api_key, pinecone_env, pinecone_index = initialize_openai_and_pinecone()

@router.post("/chat/")
async def chat(request: ChatRequest):
    # Implementación del procesamiento de chat aquí, como en tu código actual
    # ...
    return {"response": "Respuesta generada"}
