#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """
    Amenity class representattion
    """
    __tablename__ = 'amenities'

    if storage_type != 'db':
        name = ""
    else:
        name = Column(String(128), nullable=False)
