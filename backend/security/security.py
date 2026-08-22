from fastapi import Depends
from jose import jwt
from datetime import datetime, timedelta, timezone 

from dotenv import load_dotenv
load_dotenv()
import os

from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordBearer



## JWT 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

def create_access_token(user_id : int):
    expire = datetime.now(timezone.utc) + timedelta(hours=2)

    payload = {
        "sub" : str(user_id),
        "exp" : expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def get_jwt_user(token : str = Depends(oauth2_scheme)):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=ALGORITHM
    )

    user_id = int(payload["sub"])

    if not user_id:
        return {
            "msg" : "User not found"
        }
    
    return user_id


# Hash password
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto"
)

def generate_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(password : str, hash_password : str):
    return pwd_context.verify(password, hash_password)


