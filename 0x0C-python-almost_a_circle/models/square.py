#!/usr/bin/python3
"""modules"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(self, size, x, y, id)

    def __str__(self):
        """return the string"""
        return "[Square] (<id>) <x>/<y> - <size>".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    def size(self):
        return self.width
