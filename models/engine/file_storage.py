#!/usr/bin/python3
""" This is the file_storage module
It contains the FileStorage class that serializes and deserializes
It serializes instances to a JSON file, deserializes JSON file
to instances
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """ The FileStorage class
    It deals with serialization and deserialization of instances
    to and from JSO
    Methods:
    __init__(self):
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ The all method
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ The new method
        Sets in __objects the obj with key <obj class name>.id
        """
        obj_class_name = str(obj.__class__.__name__)
        my_obj = obj_class_name + "." + str(obj.id)
        self.__objects[my_obj] = obj

    def save(self):
        """ The save method
        Serializes __objects to the JSON file
        """
        my_dict = dict()
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        try:
            with open(self.__file_path, 'w') as f:
                json.dump(my_dict, f)
        except json.JSONDecodeError:
            pass

    def reload(self):
        """ The reload method
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                my_class, my_id = key.split('.')
                obj = eval(my_class)(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
