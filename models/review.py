#!/usr/bin/python3
""" This is the review module
It contains the Review class which inherits from BaseModel

It has attributes, place_id, user_id, text
"""
from base_model import BaseModel


class Review(BaseModel):
    """ The Review class
    It has attributes of the review
    """
    place_id = ""
    user_id = ""
    text = ""
