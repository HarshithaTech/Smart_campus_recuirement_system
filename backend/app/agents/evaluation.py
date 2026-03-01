import google.generativeai as genai
import os
from typing import List, Dict, Any

class EvaluationAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_interview_question(self, context: Dict[str, Any], history: List[Dict[str, str]]) -> str:
        prompt = f"""
        You are an adaptive AI Interviewer. 
        Context: {context}
        History: {history}
        Generate the next technical follow-up question. 
        Focus on technical depth and confidence.
        """
        response = self.model.generate_content(prompt)
        return response.text

    def calculate_scores(self, responses: List[Dict[str, Any]]) -> Dict[str, float]:
        # Placeholder for entropy-based confidence scoring logic
        return {
            "technical_depth": 0.85,
            "confidence": 0.90,
            "cultural_fit": 0.80,
            "entropy_score": 0.12 # Low entropy = high confidence
        }

evaluation_agent = EvaluationAgent()
