import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import chat

app = FastAPI()

# Configurar CORS para aceptar solicitudes desde el frontend en Vercel (o cualquier otro frontend)
frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")  # Cambia el valor predeterminado según tus necesidades
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://memory-gpt-frontend.vercel.app/"],  # Reemplaza con la URL de tu frontend en Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir el router de chat
app.include_router(chat.router)

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente en Railway"}
