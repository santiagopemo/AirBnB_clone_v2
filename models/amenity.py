#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
