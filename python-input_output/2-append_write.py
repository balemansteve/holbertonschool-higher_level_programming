#!/usr/bin/python3
"""
This module contains the 'append_write' function,
it append the content of a file and returns the
number of characters added
"""


def append_write(filename="", text=""):
    """
    Add a text file (UTF-8) and return the
    number of characters added
    Args:
        filename (str): The name of the file to be write
    """
    with open(filename, 'a', encoding="utf-8") as f:
        number_chars = f.write(text)
    return number_chars
