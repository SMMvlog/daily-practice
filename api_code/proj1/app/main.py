from fastapi import FastAPI,Depends,HTTPException
from app.database.db_connection import engine
from app.database import models
from app.database.db import get_db
from app.schemas import UserCreate,GetUsers,UserUpdate
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def home():
    return {"msg":"hello users"}

@app.post("/user_details")
async def create_users(user:UserCreate,db:Session=Depends(get_db)):
    try:
        existing_user = db.query(models.Users).filter(models.Users.email_id==user.email_id).first()
        if existing_user:
            return {"msg":"The email id is already registered try with different email id"}
        new_user = models.Users(name=user.name,location=user.location,email_id=user.email_id)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except Exception as ex:
        return {"msg":"something went wrong","error":str(ex)}
@app.get("/get_all_users",response_model=list[GetUsers])
async def get_users(db:Session=Depends(get_db)):
    try:
        return db.query(models.Users).all()

    except Exception as ex:
        return {"msg":"something went wrong", "error":str(ex)}
@app.patch("/update_user/{emp_id}",response_model=GetUsers)
async def update_user(emp_id:int,users:UserUpdate,db:Session=Depends(get_db)):
    try:
        existing_user = db.query(models.Users).filter(models.Users.id==emp_id).first()
        if existing_user:
            if users.name:
                existing_user.name = users.name
            if users.location:
                existing_user.location = users.location
            if users.email_id:
                existing_user.email_id = users.email_id
            db.commit()
            db.refresh(existing_user)
            return existing_user
        else:
            return HTTPException(status_code=404, detail="User not found")
    except Exception as ex:
        return {"msg":"Something went wrong","error":str(ex)}
    
@app.delete("/user_delete/{emp_id}")
async def user_delete(emp_id:int,db:Session=Depends(get_db)):
    try:
        user = db.query(models.Users).filter(models.Users.id==emp_id).first()
        if user:
            db.delete(user)
            db.commit()
            return {"msg":"user deleted Succesfully"}
        else:
            raise HTTPException(status_code=404,detail="detail not found")
    except HTTPException:
        raise

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )