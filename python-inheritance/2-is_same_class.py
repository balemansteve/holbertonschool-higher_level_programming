#!/usr/bin/python3
"""
Function to check if is an same object
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a class
    Args:
        obj: The object to check
        a_class: The class to check
    Return:
        True: if obj is instance of a_class
        False: is obj is not instance a_class
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
