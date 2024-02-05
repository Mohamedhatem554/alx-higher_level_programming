#!/usr/bin/python3
"""def lookup"""


def lookup(obj):
    """lookup for all attributes of the object

    Args:
        obj: object class
    Returns:
        Na
    """
    return [n for n in dir(obj)]

