#!/usr/bin/python3
"""3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """function: is kind of class

    Args:
        obj: the object
        a_class: the class

    Returns:
        true if the object is an instance
    """

    return isinstance(obj, a_class)
