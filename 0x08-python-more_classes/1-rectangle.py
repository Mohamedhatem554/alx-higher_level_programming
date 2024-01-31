#!/usr/bin/python3

"""empty class"""


class Rectangle:
    """define class"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): the width of the new rectangle.
            height (int):the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set width"""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val < 0:
            raise ValueError('width must be >= 0')
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
