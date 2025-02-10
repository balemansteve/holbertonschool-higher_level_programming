#!/usr/bin/python3
"""
Function to check if is an subclass

"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class or inherits from it
    (directly or indirectly).
    Args:
        obj: The object to check
        a_class: The class to check against
    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise
        """
    return True if issubclass(type(obj), a_class) \
        and type(obj) is not a_class else False
