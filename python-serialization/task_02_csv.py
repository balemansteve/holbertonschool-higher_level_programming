#!/usr/bin/python3
"""
Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON and write it to 'data.json'
    Args:
        csv_filename (str): The name of the CSV file to be converted
    Returns:
        bool: True if the conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except Exception as e:
        """
        Print an error message if conversion fails
        """
        print(f"An error occurred: {e}")
        return False
