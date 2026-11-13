from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
class UserCreate(BaseModel):
    name: str = Field(...,min_length=3,max_length=10)
    location: str |None = Field(None,min_length=3,max_length=10)
    email_id: EmailStr | None = None

class GetUsers(BaseModel):
    name: str 
    location: str 
    email_id: EmailStr
    created_at :datetime
    updated_at :datetime

class UserUpdate(BaseModel):
    name: str |None = Field(None,min_length=3,max_length=10)
    location: str |None = Field(None,min_length=3,max_length=10)
    email_id: EmailStr|None = None
