#!/usr/bin/python3
"""10-student.py"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        if attrs is None:
            return self.__dict__
        new_dic = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dic[key] = value
        return new_dic
