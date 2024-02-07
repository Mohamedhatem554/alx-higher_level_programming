#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="UTF-8") as f:
        num = f.write(text)
        return num
