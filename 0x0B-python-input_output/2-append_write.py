#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """append_write function

    Args:
        filename (str): write file name . Defaults to "".
        text (str): write text. Defaults to "".

    Returns:
        number of characters
    """
    with open(filename, "a", encoding="UTF-8") as f:
        num = f.write(text)
        return num
