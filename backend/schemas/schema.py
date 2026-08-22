from pydantic import BaseModel


class Auth(BaseModel):
    email : str
    password : str


class NoteCreate(BaseModel):
    title : str
    content : str
    status : str


class NoteUpdate(BaseModel):
    title : str
    content : str
    status : str


class UserProfile(BaseModel):
    name : str | None = None
    email : str | None = None
    password : str | None = None
    phone_no : str | None = None
    theme : str | None = None