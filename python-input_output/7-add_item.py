#!/usr/bin/python3
"""
This module contains a functions to:
    load a JSON file to a Python list
    add command-line arguments to the list
    save the updated list back to the JSON file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arg = load_from_json_file('add_item.json')
except FileNotFoundError:
    arg = []

arg.extend(sys.argv[1:])
save_to_json_file(arg, "add_item.json")
