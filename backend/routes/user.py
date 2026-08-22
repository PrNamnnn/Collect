from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from sqlalchemy import select
from schemas.schema import UserProfile

from security.security import get_jwt_user, generate_password_hash


user = APIRouter(
    prefix="/api/user",
    tags=["User"]
)


@user.get("/")
def get_my_details(
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):

    user = db.scalars(
        select(User).where(User.id == user_id)
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found!"
        )

    return {
        "name" : user.name,
        "email" : user.email,
        "password" : "*" * 10,
        "phone_no" : user.phone_no,
        "current_theme" : user.theme,
        "plan" : "Premium" if user.premium else "Basic",
        "joined_date" : user.joined_date
    }


@user.patch("/")
def update_user(
    data : UserProfile,
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):
    user = db.scalars(
        select(User).where(User.id == user_id)
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if data.name is not None:
        user.name = data.name

    if data.email is not None:
        user.email = data.email

    if data.password is not None:
        user.password_hash = generate_password_hash(data.password)

    if data.phone_no is not None:
        user.phone_no = data.phone_no

    if data.theme is not None:
        user.theme = data.theme

    db.commit()

    return {
        "msg" : "Profile updated Successfully"
    }


@user.delete("/")
def delete_profile(
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):
    user = db.scalars(
        select(User).where(User.id == user_id)
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "msg" : "User deleted successfully"
    }