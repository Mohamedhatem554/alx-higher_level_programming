#!/usr/bin/python3
"""9-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle

    Args:
        BaseGeometry (class): inherited class
    """
    def __init__(self, width, height):
        """constractor

        Args:
            width (int): the width
            height (int): the height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """function area

        Returns:
            area
        """
        return self.__width * self.__height

    def __str__(self):
        """str function

        Returns:
            width and height
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
