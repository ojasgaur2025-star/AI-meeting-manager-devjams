from fastapi import APIRouter, UploadFile, File, Depends, Query
from sqlalchemy.orm import Session
import shutil, os
from .. import crud, models, schemas
from ..database import SessionLocal, engine
from ..services.ai import transcribe_audio, summarize_text

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def create_meeting(
    file: UploadFile = File(...), 
    speaker: str = Query(None),
    db: Session = Depends(get_db)
):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcript = transcribe_audio(file_path)
    summary = summarize_text(transcript, speaker=speaker)

    meeting_data = schemas.MeetingCreate(title=file.filename, speaker=speaker)
    db_meeting = crud.create_meeting(db=db, meeting=meeting_data, owner_id=1)
    db_meeting.transcript = transcript
    db_meeting.summary = summary
    db.commit()

    os.remove(file_path)

    return {"id": db_meeting.id, "transcript": transcript, "summary": summary}

@router.get("/")
def list_meetings(db: Session = Depends(get_db)):
    return crud.get_meetings(db)

@router.get("/{meeting_id}")
def get_meeting(meeting_id: int, db: Session = Depends(get_db)):
    return crud.get_meeting(db, meeting_id)
