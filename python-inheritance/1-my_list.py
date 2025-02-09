#!/usr/bin/python3
"""
This module defines a list class
"""


class MyList(list):
    """
    This method prints the sorted list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
        return(sorted_list)
