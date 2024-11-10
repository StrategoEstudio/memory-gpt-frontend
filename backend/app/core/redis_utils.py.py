import openai
import redis
from app.core.config import settings

# Conectar a Redis usando la URL completa
redis_client = redis.StrictRedis.from_url(settings.redis_url, decode_responses=True)

def get_embedding(text):
    """Genera el embedding para un texto utilizando la API de OpenAI."""
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

def store_message_in_redis(user_id, message, embedding):
    """Almacena un mensaje y su embedding en Redis usando una lista."""
    message_data = {"message": message, "embedding": embedding}
    redis_client.lpush(f"chat_history:{user_id}", str(message_data))

def retrieve_context_from_redis(user_id, max_messages=5):
    """Recupera el contexto de los últimos mensajes del historial de Redis."""
    chat_history = redis_client.lrange(f"chat_history:{user_id}", 0, max_messages - 1)
    context = " ".join([eval(msg)["message"] for msg in chat_history])
    return context
