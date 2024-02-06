#!/usr/bin/python3
"""10-square.py"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square

    Args:
        Rectangle (class): Rectangle class
    """
    def __init__(self, size):
        """constructor

        Args:
            size (int): the size of square
        """
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """function area

        Returns:
            the area
        """
        return super().area()
