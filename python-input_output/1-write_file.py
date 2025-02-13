#!/usr/bin/python3
"""
This module contains the 'write_file' function,
it writes the content of a file and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a text file (UTF-8) and return the
    number of characters written
    Args:
        filename (str): The name of the file to be write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        number_chars = f.write(text)
    return number_chars
