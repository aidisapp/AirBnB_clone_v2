#!/usr/bin/python3
"""State Module for HBNB project"""

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state"""
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
                "City", cascade='all, delete, delete-orphan', backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """Returns the list of City instances with state_id
            equals to the current State.id"""
            all_cities = models.storage.all(City)
            return [city for city in all_cities.values(
                                    ) if city.state_id == self.id]
