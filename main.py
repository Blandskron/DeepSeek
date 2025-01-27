from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gradio_client import Client

# Crear una instancia de FastAPI
app = FastAPI()

# Inicializar el cliente de Gradio
client = Client("Blandskron/ChatBots")

# Modelo de datos para las solicitudes
class ChatRequest(BaseModel):
    message: str

# Endpoint para procesar las solicitudes
@app.post("/chat")
async def chat_with_model(request: ChatRequest):
    try:
        # Realizar la predicción usando el cliente de Gradio
        result = client.predict(
            message=request.message,
            api_name="/chat"
        )
        return {"response": result}
    except Exception as e:
        # Manejar errores
        raise HTTPException(status_code=500, detail=str(e))

# Ejecutar con Uvicorn: uvicorn main:app --reload
