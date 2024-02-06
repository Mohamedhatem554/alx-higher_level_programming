#!/usr/bin/python3
"""7-base_geometry.py"""


class BaseGeometry():
    """class base geometry"""

    def area(self):
        """function: area

        Raises:
            Exception: handle error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function: integer_validator

        Args:
            name: the name
            value: the value

        Raises:
            TypeError: handle error
            TypeError: handle error
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
