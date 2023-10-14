#!/usr/bin/python3
""" This is the state module
It contains the State class which inherits from BaseModel

It has an attribute, name, the name of the state
"""
from base_model import BaseModel


class State(BaseModel):
    """ The State class
    It has attributes of the state
    """
    name = ""
