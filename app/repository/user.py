from fastapi import APIRouter
from app.schema import ResponseBlog, ResponseUser, BaseBlog, CreateUser, Blog
from typing import Optional, List

from app.models import User, Blog
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, HTTPException
from app.database import SessionLocal, get_db


def create(request: CreateUser, db:Session):
    new_user = User( username=request.username,
                        email=request.email)
    new_user.hash_password(request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def show(id:int, db:Session):
    user = db.query(User).filter_by(id=id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user

