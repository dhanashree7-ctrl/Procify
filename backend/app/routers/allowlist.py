from fastapi import APIRouter, UploadFile, File
from ..models.schemas import AllowlistEntry
from typing import List

router = APIRouter()

@router.post("/upload-csv")
async def upload_allowlist_csv(file: UploadFile = File(...)):
    # Handle CSV upload of USNs and Emails
    return {"status": "success", "entries_added": 100}

@router.get("/list", response_model=List[AllowlistEntry])
async def get_allowlist():
    return []
