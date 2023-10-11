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
    prompt = "(hbnb) "

    def __init__(self, my_number=0, name=""):
        self.id = str(uuid.uuid4())
        self.my_number = my_number
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

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

    def do_EOF(self, line):
        """ This is the EOF method
        It enables smooth exiting upon hitting
        CTRL+d
        """
        return True

    def postloop(self):
        """The postloop method
        Can be used as a stub
        """
        print()

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
        my_dict["__class__"] = self.__class__.__name__

        return my_dict
