import google.generativeai as genai
import os
from typing import List, Dict, Any
from sqlalchemy import text
from app.db.session import SessionLocal

class SourcingAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.embedding_model = "models/text-embedding-004"

    def generate_embedding(self, text: str) -> List[float]:
        result = genai.embed_content(model=self.embedding_model, content=text)
        return result['embedding']

    async def find_matches(self, job_description: str, limit: int = 10) -> List[Dict[str, Any]]:
        job_vector = self.generate_embedding(job_description)
        db = SessionLocal()
        try:
            # Cosine similarity search using pgvector
            query = text("""
                SELECT reference_id, content, 1 - (vector_data <=> :vector) AS similarity
                FROM embeddings
                WHERE reference_type = 'resume'
                ORDER BY vector_data <=> :vector
                LIMIT :limit
            """)
            results = db.execute(query, {"vector": str(job_vector), "limit": limit}).fetchall()
            return [{"candidate_id": r[0], "match_score": float(r[2])} for r in results]
        finally:
            db.close()

sourcing_agent = SourcingAgent()
