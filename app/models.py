from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base, engine
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    blogs = relationship('Blog', back_populates='creator')

    
    def hash_password(self, input_password):
        self.hashed_password = pwd_context.hash(input_password)
        return self.hashed_password

    # @hash_password.setter
    # def hash_password(self, input_password):
    #     self.hash_password = pwd_context.hash(input_password)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.hashed_password)

    
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    creator_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='blogs')

Base.metadata.create_all(engine)