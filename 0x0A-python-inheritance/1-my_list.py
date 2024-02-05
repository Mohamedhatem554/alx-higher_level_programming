#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """the class inherits from list()

    Args:
        list: The list
    """

    def print_sorted(self):
        """prints the sorted list"""

        print(sorted(self))
