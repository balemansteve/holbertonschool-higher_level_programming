#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """A class that inherits from list
    Arg: 'list': The parent class
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
