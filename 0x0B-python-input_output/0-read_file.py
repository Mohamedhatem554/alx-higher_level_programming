#!/usr/bin/python3
"""define function"""


def read_file(filename=""):
    """ readfile function

    Args:
        filename (str): write a file name. Defaults to NULL.
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print("{:s}".format(f.read()), end="")
