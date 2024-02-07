#!/usr/bin/python3
"""100-append_after.py"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    dic = []
    with open(filename, "r", encoding="UTF-8") as f:
        dic = f.readlines()
        i = 0
        while i < len(dic):
            if search_string in dic[i]:
                dic[i:i + 1] = [dic[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="UTF-8") as a:
        a.writelines(dic)
