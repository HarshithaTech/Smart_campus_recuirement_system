from fastapi import APIRouter, Depends, HTTPException, status
from app.agents.supervisor import supervisor_agent
from app.agents.sourcing import sourcing_agent
from app.agents.evaluation import evaluation_agent
from app.agents.integrity import integrity_agent
from typing import Dict, Any, List

router = APIRouter(prefix="/agents", tags=["agents"])

@router.post("/process")
async def process_request(intent: str, context: Dict[str, Any]):
    return await supervisor_agent.process_request(intent, context)

@router.post("/source")
async def source_candidates(job_description: str):
    return await sourcing_agent.find_matches(job_description)

@router.post("/verify")
async def verify_credentials(data: Dict[str, Any]):
    return integrity_agent.verify_credential(data)

@router.post("/interview/question")
async def get_question(context: Dict[str, Any], history: List[Dict[str, str]]):
    return await evaluation_agent.generate_interview_question(context, history)
