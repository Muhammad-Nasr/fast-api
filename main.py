from fastapi import FastAPI
from app.router import user, blog, authentication

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)