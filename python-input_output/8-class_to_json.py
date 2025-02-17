#!/usr/bin/python3
"""
This module contains the 'class_to_json' function
it converts an object attributes into a dictionary
"""


def class_to_json(obj):
    """
    Converts an object attributes into a dictionary
    Args:
        obj (object): The instance of a class to convert
    Returns:
        dict: A dictionary containing the object attributes
    """
    arguments = {}
    for key, value in obj.__dict__.items():
        arguments[key] = value
    return arguments
