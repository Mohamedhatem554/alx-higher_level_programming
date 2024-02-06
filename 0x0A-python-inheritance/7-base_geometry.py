#!/usr/bin/python3
"""7-base_geometry.py"""


class BaseGeometry:
    """class base geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if type(value) <= 0:
            raise TypeError(name + " must be greater than 0")
