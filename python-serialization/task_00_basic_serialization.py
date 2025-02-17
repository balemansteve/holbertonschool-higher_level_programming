#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize data and save it to the specified file
    Args:
        data: The data to be serialized
        filename (str): The name of the file to save the data
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file
    Args:
        filename (str): The name of the file to load the data from
    Returns:
        data: The deserialized data from the file
    """

    with open(filename, 'r') as f:
        data = json.load(f)
    return data
