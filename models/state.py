#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String



class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """
            It will be the FileStorage relationship between State and
            City
            """
            from models import storage

            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
