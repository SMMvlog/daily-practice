from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/home/{user_name}")
def home(user_name):
    return {"msg":f"Hello {user_name}"}


class InfoGet(BaseModel):
    name:str
    age:int
    location:str

@app.post("/get_info")
def get_info(info:InfoGet):
    return {"msg":f"Hello {info.name} your age is {info.age} and your location is {info.location}"}