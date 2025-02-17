#!/usr/bin/python3
"""
This module contains a 'Student' class
which can be converted into a dictionary
representation (JSON format)
"""


class Student:
    """
    Student class with attributes and method to
    retrieve a dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance
        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of the Student instance
        Args:
            attrs (list, optional):
                List of attributes to include
                If None, all attributes are included
        Returns:
            dict: Dictionary with specified
            attributes or all attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value
                    in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Student class to JSON
        Args:
            json: Dictionary representation of a simple data structure
        """
        for key, value in json.items():
            setattr(self, key, value)
