#!/usr/bin/python3

def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        words = (delimeter + "\n\n").join(
            [index.strip(" ") for index in words.split(delimeter)])
