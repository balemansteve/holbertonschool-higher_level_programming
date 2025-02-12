#!/usr/bin/python3
"""
This module contains the 'read_file' function,
it reads the content of a file and prints it to the standard output
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints this content
    Args:
        filename (str): The name of the file to be read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
