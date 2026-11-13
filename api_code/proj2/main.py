from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from pydantic import EmailStr,BaseModel,Field
from datetime import datetime

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/mehboob"

app = FastAPI(docs_url = "/api_docs")


engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    user_name:str
    location:str
    mobile_number: str = Field(
        pattern=r"^[6-9]\d{9}$"
    )
    email_id:EmailStr
class UserResponse(BaseModel):
    id: int
    user_name: str
    mobile_number: str
    location: str
    email_id: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 

class UserMaster(base):
    __tablename__ = "user_master"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    mobile_number = Column(String(15), unique=True, nullable=False)
    location = Column(String(100))
    email_id = Column(String(100), unique=True, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return {"msg":"Hello Users"}

@app.post("/user_create")
async def user_create(user:UserCreate,db:Session=Depends(get_db)):
    existing_user = db.query(UserMaster).filter(UserMaster.email_id==user.email_id).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already Exist")
    new_user = UserMaster(
        user_name = user.user_name,
        email_id = user.email_id,
        location = user.location,
        mobile_number = user.mobile_number
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
