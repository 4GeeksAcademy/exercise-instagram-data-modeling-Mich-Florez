import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name=Column(String(250), nullable=False)
    last_name=Column(String(250), nullable=False)
    email=Column(String(250), nullable=False)
    relation_follower = relationship("Follower", backref="user")
    relation_comment = relationship("Comment", backref="user")
    relation_post = relationship("Post", backref="user")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(ForeignKey("user.id"))
    user_to_id = Column(ForeignKey("user.id"))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    relation_media = relationship("Media", backref="post")
    relation_comment = relationship("Comment", backref="post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(ForeignKey("user.id"), nullable=False)
    post_id = Column(ForeignKey("post.id"), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(ForeignKey("post.id"), nullable=False)      
    
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
