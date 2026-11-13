from fastapi import FastAPI,Depends,BackgroundTasks,HTTPException,Request,Query
from sqlalchemy import create_engine,Column,Integer,String,func,DateTime,Boolean,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,Session,relationship,selectinload
from typing import Optional
from pydantic import EmailStr,ConfigDict,BaseModel,Field,field_validator
from datetime import datetime
from app.utils import send_greeting_email,authenticate
from dotenv import load_dotenv
import os
from app.jwt_config import create_access_token
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL,echo=True)

Base = declarative_base()
LocalSession = sessionmaker(bind=engine,autoflush=False,autocommit=False)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


class UserMaster(Base):
    __tablename__ = "user_master_new"
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    email_id = Column(String(150),nullable=False,unique=True)
    is_active = Column(Boolean,default=True)
    location = Column(String(150),nullable=True)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_default=func.now(),onupdate=func.now())
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "order_master"
    id = Column(Integer,primary_key=True)
    product_name = Column(String,nullable=False)
    quantity = Column(Integer,nullable=False)
    user_id = Column(Integer,ForeignKey("user_master_new.id"),nullable=False)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_default=func.now(),onupdate=func.now())
    user = relationship("UserMaster", back_populates="orders")

class OrderRequest(BaseModel):
    product_name : str =  Field(min_length=3,max_length=100)
    quantity : int
    user_id : int

class UserRequest(BaseModel):
    name:str
    email_id:EmailStr
    is_active:bool
    location:Optional[str]=None

class UserResponse(BaseModel):
    name:str
    email_id:EmailStr
    is_active:bool
    location:Optional[str] = None
    created_at:datetime
    updated_at:datetime
    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    user_id:int
    email_id:str = Field(min_length=10,max_length=120)

    @field_validator("email_id")
    @classmethod
    def validate_email(cls,value):
        if not value.endswith("@gmail.com"):
            raise ValueError("Only Gmail address are allowed")
        return value

    @field_validator("user_id")
    @classmethod
    def validate_user_id(cls,value):
        if value <=0:
            raise ValueError("Give proper user ID")
        return value

         

Base.metadata.create_all(bind=engine)


@app.post("/add_user",response_model=UserResponse)
@authenticate
async def add_user_data(request: Request,user:UserRequest,background_task:BackgroundTasks,db:Session=Depends(get_db)):
    new_user = UserMaster(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    background_task.add_task(send_greeting_email,user.email_id,user.name)
    return new_user


@app.get("/get_users",response_model=list[UserResponse])
@authenticate
async def get_users(request: Request,page:int=Query(1,ge=1),limit:int=Query(10,ge=1,le=100),name:str | None = None,city:str | None=None,db:Session=Depends(get_db)):
    print("user_id",request.state.user_id)
    user_data = db.query(UserMaster)
    if name:
        user_data = user_data.filter(UserMaster.name.ilike(f"%{name}%"))
    if city:
        user_data = user_data.filter(UserMaster.location.ilike(f"%{city}%"))

    offset = (page-1)*limit

    if user_data:
        user_data = user_data.offset(offset).limit(limit).all()
        return user_data
    else:
        raise HTTPException(detail="User not found",status_code=404)

@app.post("/create_order")
@authenticate
async def get_order_created(request:Request,order:OrderRequest,db:Session=Depends(get_db)):
    user = db.query(UserMaster).filter(UserMaster.id==order.user_id).first()
    if not user:
        raise HTTPException(detail="user does not Exist",status_code=404)
    order_create = Order(**order.model_dump())
    db.add(order_create)
    db.commit()
    db.refresh(order_create)

    return {
        "msg": "Order Created Successfully",
        "order_id": order_create.id
    }

@app.post("/login")
async def get_login(get_login:LoginRequest,db:Session=Depends(get_db)):
    user = db.query(UserMaster).filter(UserMaster.id==get_login.user_id , UserMaster.email_id==get_login.email_id).first()
    if user:
        token = create_access_token({"user_id":user.id,"email_id":user.email_id})
        if token:
            return {"msg":"User Login Successfully","token":f"Bearer {token}","token_type":"Bearer"}
        return {"msg":"something went wrong"},400
    raise HTTPException(status_code=404,detail="User not found")

@app.get("/order/user_id")
async def get_orders(user_id:int,db:Session=Depends(get_db)):
    # user_orders = db.query(Order).filter(Order.id==user_id).all()

    print("start---------------------------------")
    users = db.query(UserMaster).options(selectinload(UserMaster.orders)).all()

    print("rter--",users)
    for user in users:
        print(user.orders)

    return {"msg":"Success"}
