#!/usr/bin/python3
"""11-square.py"""


Rectangle = __import__('9-rectangle').Rectangle

"""square class"""


class square(Rectangle):
    """class square

    Args:
        Rectangle (class): Rectangle class
    """
    def __init__(self, size):
        """constructor

        Args:
            size (int): square size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """function str

        Returns:
            Square size
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size,)
