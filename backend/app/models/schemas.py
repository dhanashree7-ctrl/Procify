from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    usn: Optional[str] = None
    role: str

class UserLogin(BaseModel):
    identifier: str  # Email or USN
    session_code: str

class SessionCreate(BaseModel):
    title: str
    type: str  # 'exam' or 'interview'
    start_time: datetime
    duration_minutes: int

class SessionResponse(BaseModel):
    id: str
    title: str
    status: str
    session_code: str

class AllowlistEntry(BaseModel):
    identifier: str
    name: Optional[str] = None

class ReportResponse(BaseModel):
    report_id: str
    student_id: str
    score: float
    violations: List[Dict[str, Any]]
