import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from functools import wraps
from fastapi import Request,HTTPException
from app.jwt_config import decode_token
load_dotenv()


def send_greeting_email(email: str, name: str):

    message = MIMEText(
        f"Hello {name}, welcome to our application!"
    )

    message["Subject"] = "Welcome!"
    message["From"] = os.getenv("EMAIL")
    message["To"] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()

        server.login(
            os.getenv("EMAIL"),
            os.getenv("EMAIL_PASSWORD")
        )

        server.send_message(message)

def authenticate(func):
    @wraps(func)
    async def wrapper(request:Request,*args,**kwargs):
        auth_token = request.headers.get("Authorization")

        if not auth_token:
            raise HTTPException(status_code=401,detail="Authorization Header Missing")

        if not auth_token.startswith("Bearer "):
            raise HTTPException(status_code=401,detail="Invalid Token")

        token = auth_token.split(" ",1)[1]
        print("token--",token)
        decoded = decode_token(token)
        if not decoded:
            raise HTTPException(status_code=401,detail="Invalid Token")
        print("decoded---",decoded)
        request.state.user_id = decoded.get("user_id")

        return await func(request,*args,**kwargs)

    return wrapper
        

        