#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """This class defines a user by various attributes:
	email: email address
        password: password for you login
        first_name: first name
        last_name: last name
	"""
	__tablename__ = "users"
	email = Column(String(128), nullable=False)
	password = Column(String(128), nullable=False)
	first_name = Column(String(128))
	last_name = Column(String(128))
	places = relationship("Place", backref="user", cascade="delete")
	reviews = relationship("Review", backref="user", cascade="delete")
