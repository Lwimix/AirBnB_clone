#!/usr/bin/python3
""" This is the city module
It contains the City class which inherits from BaseModel

It has attributes, name, and state_id
"""
from base_model import BaseModel


class City(BaseModel):
    """ The City class
    It has attributes of the city
    """
    state_id = ""
    name = ""
