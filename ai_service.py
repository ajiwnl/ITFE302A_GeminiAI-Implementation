import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment")
        
        genai.configure(api_key=api_key)
        # Using the standard alias for the latest Flash model (Free Tier)
        self.model = genai.GenerativeModel("gemini-flash-latest")

    async def get_response(self, prompt: str):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error communicating with Gemini: {str(e)}"

    async def analyze_data(self, data: str):
        prompt = f"Analyze the following data and provide insights:\n\n{data}"
        return await self.get_response(prompt)
