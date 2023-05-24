from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import create_engine

# from db import Base
from sqlalchemy.orm import sessionmaker

# from models import User, Post
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f"User(user_id={self.user_id}, first_name='{self.first_name}', last_name='{self.last_name}')"


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    date = Column(DateTime, default=datetime.now)
    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post(post_id={self.post_id}, user_id={self.user_id}, date={self.date})"
