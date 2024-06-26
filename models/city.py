#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """
    This is the class for City
    Attributes:
        __tablename__: private attribute name for the table
        state_id: The state id
        name: input name
        places: foreign key for the places model
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
