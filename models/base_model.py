#!/usr/bin/python3
""" This is the base_model module
It contains the basemodel class
with all common attributes or methods
for other classes
"""
import uuid
from datetime import datetime, timezone


class BaseModel():
    """ This is my base class
    It holds all attributes and methods
    to be inherited by other classes
    Methods:
    __init__()
    """

    available = 0
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if args:
            self.my_number = args
            self.name = args
        if kwargs:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            available = 1
        else:
            self.created_at = str(datetime.utcnow())
            self.updated_at = str(datetime.utcnow())

    def __str__(self):
        """ This is the string magic method
        It returns a string representation of BaseModel
        """
        return "[" + self.__class__.__name__ + "] " + \
               "(" + self.id + ") " + str(self.__dict__)

    def save(self):
        """ This is the save method
        It updates the public instance attribute updated_at
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """to_dict method
        This method returns a dictionary representation
        of the class
        """
        self.__dict__.pop('cmdqueue', None)
        self.__dict__.pop('stdin', None)
        self.__dict__.pop('completekey', None)
        self.__dict__.pop('stdout', None)
        my_dict = self.__dict__
        if not self.available:
            my_dict["__class__"] = self.__class__.__name__

        return my_dict
