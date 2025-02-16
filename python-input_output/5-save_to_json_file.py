#!/usr/bin/python3
"""
This module contains the 'save_to_json_file' function,
it save the Python structure to JSON file
"""
import json

def save_to_json_file(my_obj, filename, encoding='utf-8'):
    """
    Saves the Python structure to JSON file
    Args:
        my_obj (Any): Python structure
        filename (str): The name of the file to be write
    """
    with open(filename, 'w') as f:
        if isinstance(my_obj, set):
            my_obj = list(my_obj)
        json.dump(my_obj, f)
