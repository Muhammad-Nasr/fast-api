from fastapi import APIRouter
from app.schema import ResponseBlog, ResponseUser, BaseBlog, CreateUser, Blog
from typing import Optional, List

from app.models import User, Blog
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, HTTPException
from app.database import SessionLocal, get_db
from app.repository import user


router = APIRouter(
    prefix='/user',
    tags= ['User']
)



@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: CreateUser, db: Session = Depends(get_db)):
    return user.create(request, db)
     
    


@router.get('/{id}', response_model=ResponseUser)
def get_user(id:int, db: Session = Depends(get_db)):
   return user.show(id, db)