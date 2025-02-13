#!/usr/bin/python3
"""
This module contains the 'to_json_string' function,
it converts the Python data structures into a JSON string
"""
import json


def to_json_string(my_obj):
    """
    Converts the Python data structures into a JSON string
    Args:
        my_obj (Any): Python data structure
    """
    data = json.dumps(my_obj)
    return data
