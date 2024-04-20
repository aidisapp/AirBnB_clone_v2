#!/usr/bin/python3
"""
State Module for HBNB project
Defines the Amenities model

"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    This is the class for Amenity
    Attributes:
        name: input name
        __tablename__: private attribute name for the  table
        place_amenities: foreign key to the place model
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
