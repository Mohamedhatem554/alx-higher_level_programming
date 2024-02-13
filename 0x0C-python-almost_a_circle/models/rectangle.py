#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def width(self):
        '''Width of this rectangle.'''
        return self.__width


    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value


    def height(self):
        '''Height of this rectangle.'''
        return self.__height


    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value


    def x(self):
        '''x of this rectangle.'''
        return self.__x


    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value


    def y(self):
        '''y of this rectangle.'''
        return self.__y


    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
