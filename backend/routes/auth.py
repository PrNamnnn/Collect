from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schema import Auth
from sqlalchemy import select
from database import get_db

from models.user import User

from security.security import generate_password_hash, create_access_token, verify_password



auth = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)




## Routes

@auth.post("/login")
async def login(
    data : Auth, 
    db : Session = Depends(get_db)
    ):
    
    email = data.email
    password = data.password

    user = db.scalars(
        select(User).where(User.email == email)
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(user_id=user.id)

    return {
        "token" : token,
        "token_type" : "bearer",
        "msg" : "Login Successful."
    }


@auth.post('/register')
def register(
    data : Auth,
    db : Session = Depends(get_db)
):
    email = data.email
    password = data.password

    user = db.scalars(
        select(User).where(User.email == email)
    ).first()

    if user :
        pass

    user = User(email = email, password_hash = generate_password_hash(password))

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except:
        db.rollback()
        raise


    return {
        "msg" : "Registration Successfully"
    }