from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_service import GeminiService
import uvicorn

app = FastAPI(
    title="Gemini AI API",
    description="A FastAPI backend for AI Chatbot and Analytics using Google Gemini",
    version="1.0.0"
)

# Initialize the Gemini service
gemini_service = GeminiService()

class ChatRequest(BaseModel):
    message: str

class AnalyticsRequest(BaseModel):
    dataset: str

@app.get("/")
def read_root():
    return {"message": "Gemini AI API is running!"}

@app.post("/chat")
async def chat_with_gemini(request: ChatRequest):
    """
    Send a message to Gemini and get a response.
    """
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    response_text = await gemini_service.get_response(request.message)
    return {"response": response_text}

@app.post("/analytics")
async def analyze_with_gemini(request: AnalyticsRequest):
    """
    Send a dataset to Gemini and get insights.
    """
    if not request.dataset:
        raise HTTPException(status_code=400, detail="Dataset cannot be empty")
    
    analysis = await gemini_service.analyze_data(request.dataset)
    return {"analysis": analysis}

if __name__ == "__main__":
    # In practice, usually run with uvicorn directly from cli:
    # uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
