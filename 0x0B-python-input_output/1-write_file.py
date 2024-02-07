#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """function write file

    Args:
        filename (str): write file name here. Defaults to "".
        text (str): write text. Defaults to "".

    Returns:
        number of characters
    """
    with open(filename, "w", encoding="UTF-8") as f:
        num = f.write(text)
        return num
