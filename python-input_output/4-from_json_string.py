#!/usr/bin/python3
"""
This module contains the 'to_json_string' function,
it converts the JSON string into Python data structures
"""
import json


def from_json_string(my_str):
    """
    Converts the JSON string into Python data structures
    Args:
        my_str (Any): JSON string
    """
    data = json.loads(my_str)
    return data
