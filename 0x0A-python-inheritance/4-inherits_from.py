#!/usr/bin/python3
"""4-inherits_from.py"""


def inherits_from(obj, a_class):
    """function: inherits_from

    Args:
        obj : object
        a_class : the class

    Returns:
        True if the object is an instance of a class that inherited
    """
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    return False
