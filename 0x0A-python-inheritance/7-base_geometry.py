#!/usr/bin/python3
"""7-base_geometry.py"""


class BaseGeometry:
    """class base geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if type(value) <= 0:
            raise TypeError("{:s} must be greater than 0".format(name))
