# Gemini AI Project ITFE302A_GeminiAI-Implementation
Sample implementation of Google Gemini AI for ITFE302A, focusing on API integration, backend logic, and practical use cases for AI-driven applications.

This project uses **FastAPI** to provide endpoints for an AI Chatbot and Data Analytics, integrated with **Google Gemini-1.5-Flash**.

## Project Structure

- `main.py`: FastAPI application with endpoints for chat and analytics.
- `ai_service.py`: Service class to handle interactions with the Google Gemini API.
- `.env`: Environment variables (API Key).
- `venv/`: Python 3.12 virtual environment.
- `requirements.txt`: Project dependencies.

## Prerequisites

- Python 3.12 (already used to create the virtual environment).

## Getting Started

1.  **Activate the Virtual Environment**:
    - Windows: `.\venv\Scripts\activate` or just run the provided scripts using the venv's python.
2.  **Run the Server**:
    - `.\venv\Scripts\uvicorn main:app --reload`
3.  **Access the API**:
    - Interactive docs (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)
    - Root: [http://localhost:8000/](http://localhost:8000/)

## API Endpoints

### 1. Chatbot (`/chat`)
- **Method**: `POST`
- **Payload**: `{"message": "Your message here"}`
- Interaction with Gemini for a conversational response.

### 2. Analytics (`/analytics`)
- **Method**: `POST`
- **Payload**: `{"dataset": "Your data here"}`
- Gemini will analyze the data and provide insights.
