
## create schema
from re import S
from pydantic import BaseModel
from typing import List, Optional




# create response schema
class BaseBlog(BaseModel):
    title: str
    description: str

  
class Blog(BaseModel):
    title: str
    description: str
    class Config:
        orm_mode = True   

class CreateUser(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
    

# create schema (resquest body) 

# schema for response user
class ResponseUser(BaseModel):
    username: str
    email: str
    blogs: list[Blog] = []
    class Config:
        orm_mode = True

   # create response model blog
class ResponseBlog(BaseModel):
    title: str
    description: str
    creator: CreateUser
    
    class Config:
        orm_mode = True

# create schemas for login system 

class UserSchema(BaseModel):
    username: str

class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None