from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True


# Meeting Schemas
class MeetingBase(BaseModel):
    title: str
    speaker: Optional[str] = None

class MeetingCreate(MeetingBase):
    pass

class Meeting(MeetingBase):
    id: int
    date: datetime
    transcript: Optional[str] = None
    summary: Optional[str] = None
    owner_id: int

    class Config:
        orm_mode = True
