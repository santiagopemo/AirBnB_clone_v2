#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Returns the list of City instances"""
            cities = models.storage.all(City)
            state_cities = []
            for city in cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
