from sqlalchemy import Column,String,Integer,DateTime,func
from app.database.db_connection import Base

class Users(Base):
    __tablename__ = "user_master"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    location = Column(String(100),nullable=True)
    email_id = Column(String(100),nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
