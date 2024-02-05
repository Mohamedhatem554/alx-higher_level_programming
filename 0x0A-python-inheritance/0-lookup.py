#!/usr/bin/python3

"""def lookup"""

def lookup(obj):
    """look for all attributes of the object

        Args:
            obj: object class
        Returns:
            N
    """
    return [n for n in dir(obj)]