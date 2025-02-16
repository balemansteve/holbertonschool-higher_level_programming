#!/usr/bin/python3
"""
This module contains the 'load_from_json_file' function
it load JSON file to Python structure
"""
import json


def load_from_json_file(filename):
    """
    Load a JSON file into Python structure
    Args:
        filename (str): The name of the file to be open
    Return: Python object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
