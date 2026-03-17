from fastapi import APIRouter, HTTPException
from ..models.schemas import SessionCreate, SessionResponse
from typing import List

router = APIRouter()

@router.post("/create", response_model=SessionResponse)
async def create_session(session: SessionCreate):
    # Logic to create and activate exams/interviews
    return {"id": "s1", "title": session.title, "status": "active", "session_code": "PRO123"}

@router.get("/active", response_model=List[SessionResponse])
async def list_active_sessions():
    return []
