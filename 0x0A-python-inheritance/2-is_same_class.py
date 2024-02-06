#!/usr/bin/python3
"""2-is_same_class"""


def is_same_class(obj, a_class):
    """define funcion

    Args:
        obj:object
        a_class: first class

    Returns:
        type
    """
    if type(obj) is a_class:
        return True
    return False
