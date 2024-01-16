#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models import storage_type
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship

if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay
    Class Attributes:
        __tablename__ : the mapping table
        city_id: String | user_id: String
        name: String | description: String
        number_rooms: Integer | number_bathrooms : Integer
        max_guest: Integer | price_by_night: Integer
        latitude: Float | longitude: Float
    """
    __tablename__ = 'places'

    if storage_type != 'db':
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter for reviews relationship"""
            from models import storage

            all_reviews = storage.all("Review")
            return [review for review in all_reviews
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """getter for amenities attribute"""
            from models import storage
            all_amenities = storage.all(Amenity)
            return [amenity for amenity in all_amenities
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """setter for amenities attribute"""
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
    else:
        city_id = Column(String(60), ForeignKey('cities.id'),
                         nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'),
                         nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 backref='place_amenities')