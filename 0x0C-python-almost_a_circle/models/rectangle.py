#!/usr/bin/python3
"""modules"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    def width(self):
        return self.__width

    def width(self, v):
        self.validate_integer("width", v, False)
        self.__width = v

    def height(self):
        return self.__height

    def height(self, v):
        self.validate_integer("height", v, False)
        self.__height = v

    def x(self):
        return self.__x

    def x(self, v):
        self.validate_integer("x", v, False)
        self.__x = v

    def x(self, v):
        return self.__x

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
