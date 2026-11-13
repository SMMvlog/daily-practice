from datetime import datetime, timedelta, timezone
from jose import jwt,JWTError

SECRET_KEY = "Mehboob@123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    try:
        payload = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload["exp"] = expire

        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )
    except Exception as ex:
        print("ex---",ex)
        return None

# token = create_access_token({"sub": "123",
#     "email": "mehboob@123gmail.com","location":"Mumbai"})

# print("token--",token)

def decode_token(token):
    try:
        decoded_payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return decoded_payload

    except JWTError as e:
        print("Token decode error:", e)
        return None
