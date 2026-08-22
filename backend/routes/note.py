from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schema import NoteCreate, NoteUpdate
from sqlalchemy import select
from database import get_db

from services.ai_services import generate_summary, combined_summary, generate_title

from models.note import Note

from security.security import get_jwt_user


note = APIRouter(
    prefix="/api/note",
    tags=["Note"]
)

@note.get('/')
def get_my_notes(
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
    ):

    notes = db.scalars(
        select(Note).where(Note.user_id == user_id)
    ).all()

    if not notes:
        return []

    data = []
    for note in notes:
        data.append(
            {
                "title" : note.title,
                "content" : note.content,
                "created_date" : note.created_date,
                "last_edited" : note.last_edited,
                "status" : note.status
            }
        )

    return data


# @note.get('/all')
# def get_all_notes(
#     db : Session = Depends(get_db)
#     ):

#     notes = db.scalars(
#         select(Note)
#     ).all()

#     if not notes:
#         return []

#     data = []
#     for note in notes:
#         data.append(
#             {
#                 "title" : note.title,
#                 "content" : note.content,
#                 "created_date" : note.created_date,
#                 "last_edited" : note.last_edited,
#                 "status" : note.status
#             }
#         )

#     return data


@note.post("/")
def create_note(
    data : NoteCreate,
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):
    if not data.title:
        title = generate_title(data.content)
    else:
        title = data.title

    note = Note(
        title = title,
        status = data.status,
        user_id = user_id,
        content = data.content
    )

    db.add(note)
    db.commit()

    return {
        "msg" : "Note created successfully"
    }

@note.patch('/{note_id}')
def update_note(
    note_id : int,
    data : NoteUpdate,
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):
    note = db.scalars(
        select(Note).where(Note.id == note_id, Note.user_id == user_id)
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    
    if data.content is not None:
        note.content = data.content
        if data.title is None:
            note.title = generate_title(data.content)

    if data.title is not None:
        note.title = data.title

    if data.status is not None:
        note.status = data.status

    db.commit()

    return {
        "msg" : "Note updated Successfully"
    }


@note.delete('/{note_id}')
def delete_note(
    note_id : int,
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):
    note = db.scalars(
        select(Note).where(Note.id == note_id, Note.user_id == user_id)
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    db.delete(note)
    db.commit()

    return {
        "msg" : "Note Deleted Successfully"
    }


@note.delete('/')
def delete_mul_notes(
    note_ids : list[int],
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):
    for note_id in note_ids:
        
        note = db.scalars(
            select(Note).where(Note.id == note_id, Note.user_id == user_id)
        ).first()

        if not note:
            raise HTTPException(
                status_code=404,
                detail="Note not found"
            )

        db.delete(note)
    db.commit()

    return {
        "msg" : "Notes Deleted Successfully"
    }


# AI services routes

@note.get("/summary")
def all_summary(
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):
    notes = db.scalars(
        select(Note).where(Note.user_id == user_id)
    ).all()

    if not notes:
        raise HTTPException(
                status_code=404,
                detail="No Notes found"
            )
    contents = [note.content for note in notes]

    summary = combined_summary(contents)

    return {
        "summary" : summary
    }


@note.get("/{note_id}/summary")
def note_summary(
    note_id : int,
    user_id : int = Depends(get_jwt_user),
    db : Session = Depends(get_db)
):
    note = db.scalars(
        select(Note).where(Note.id == note_id, Note.user_id == user_id)
    ).first()

    if not note:
        raise HTTPException(
                status_code=404,
                detail="Note not found"
            )

    summary = generate_summary(note.content)

    return {
        "summary" : summary
    }