from fastapi import APIRouter
from app.schema import ResponseBlog, ResponseUser, BaseBlog, CreateUser, Blog
from typing import Optional, List
from app.database import get_db

from app.models import User, Blog
from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, HTTPException
from app.database import SessionLocal



def create(db: Session, request_body):
    new_blog = Blog(title=request_body.title,
                description=request_body.body, 
                creator_id=1)
    
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id:int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the blog with {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return "done"


def show(id:int, db:Session):
    blog = db.query(Blog).filter_by(id =id).first()
    if not blog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'error': f"the id {id} is not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"bolg with id {id} is not found")
    return blog

# update blog by id
def update(id:int, request_body: BaseBlog, db: Session):
    blog = db.query(Blog).filter(Blog.id ==id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"the blog {id} is not found")
    
    blog.update(request_body.dict())
    db.commit()
    return 'update successfully'


def get_all(db:Session):
    all_blogs = db.query(Blog).all()
    return all_blogs