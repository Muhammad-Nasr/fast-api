from fastapi import APIRouter
from app.schema import ResponseBlog, ResponseUser, BaseBlog, CreateUser, Blog, UserSchema
from typing import Optional, List
from app.database import get_db
from app.repository import blog, user
from app.models import User, Blog
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, HTTPException
from app.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from app.auth import auth


router = APIRouter(
    prefix= '/blog',
    tags= ['Blog']
)




@router.post('/blog', response_model=ResponseBlog)
def create_blog( request_body: BaseBlog, db: Session = Depends(get_db),
                    current_user: UserSchema = Depends(auth.get_current_user)):
    return blog.create(db, request_body)


@router.get('/blog/{id}')
def show_blog(id:int, response: Response, db: Session = Depends(get_db),
                current_user: UserSchema = Depends(auth.get_current_user)):
  return blog.show(id, db)

    

@router.get('/blogs', status_code=status.HTTP_202_ACCEPTED, response_model=list[ResponseBlog])
def get_all(db: Session = Depends(get_db), current_user: UserSchema = Depends(auth.get_current_user)):
   return blog.get_all(db)


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(get_db), current_user: UserSchema = Depends(auth.get_current_user)):
   return blog.delete(id, db)


@router.put('/blog/{id}')
def update(id, request_body: BaseBlog, db: Session = Depends(get_db), current_user: UserSchema = Depends(auth.get_current_user)):
    return blog.update(id, request_body, db)
    
