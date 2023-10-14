#!/usr/bin/python3
""" This is the user module
It contains the User class which inherits from BaseModel
It has attributes such as email, password, first_name,
last_name
"""
from base_model import BaseModel


class User(BaseModel):
    """ The User class
    It has attributes of our user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
