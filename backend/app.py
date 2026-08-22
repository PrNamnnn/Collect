from fastapi import FastAPI
from models.base import Base
from database import engine

from routes.auth import auth as auth_router
from routes.user import user as user_router
from routes.note import note as note_router

from models.user import User
from models.follow import Follow
from models.friends import FriendShip
from models.note import Note


app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(note_router)

Base.metadata.create_all(bind=engine)