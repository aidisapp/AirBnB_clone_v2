#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances and persist them
    Attributes:
        __file_path: path to the JSON file
        __objects: objects to be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or objects of a specified class.
        Args:
            cls (class, optional): The class of objects to return.
        Defaults to None.
        Returns:
            dict: A dictionary of objects.
        """
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """
        Sets __objects to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if file exists)
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                jo = json.load(f)
            for key, value in jo.items():
                self.__objects[key] = classes[value["__class__"]](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it’s inside
        Args:
            obj (optional): The object to delete. Defaults to None.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """
        Calls reload() method for deserializing the JSON file to objects
        """
        self.reload()
