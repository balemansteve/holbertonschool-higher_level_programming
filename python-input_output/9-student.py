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
        Retrieves a dictionary representation of the Student instance
        Args:
            attrs (list, optional):
                A list of attributes names include
                If None, all attributes are included
        Returns:
            dict: A dictionary containing the specified attributes or
            all attributes
        """
        return self.__dict__
