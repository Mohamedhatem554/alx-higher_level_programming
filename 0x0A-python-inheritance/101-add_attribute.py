#!/usr/bin/python3
"""define function"""


def add_attribute(obj, att, value):
    """function: add_attribute

    Args:
        obj : object_
        att (str): attribute
        value (int): value

    Raises:
        TypeError: handle error
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
