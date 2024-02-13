#!/usr/bin/python3
"""modules for base class"""
from json import dumps, loads
import csv


class Base:
    """define class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """define constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        """from json string"""
        if json_string in None or not json_string:
            return []
        return loads(json_string)
