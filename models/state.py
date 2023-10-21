#!/usr/bin/python3
""" This is a class State"""
import models
import os
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This represents a state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializing the state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """Its a getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(models.City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(value)
            return city_list
