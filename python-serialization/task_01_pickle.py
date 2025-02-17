#!/usr/bin/python3
"""
Pickling Custom Classes
"""
import pickle 


class CustomObject:
    """
    A custom object with attributes name, age, and is_student
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the object with the given name, age, and is_student values
        Args:
            name (str): The name of the object
            age (int): The age of the object
            is_student (bool): Whether the object represents a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's name, age, and is_student attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file
        Args:
            filename (str): The name of the file to save the object to
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            """
            Print an error message if serialization fails
            """
            print(f"An error occurred while serializing: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize the object from a file
        Args:
            filename (str): The name of the file to load the object from
        Returns:
            CustomObject: The deserialized object, or None if it fails
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            """
            Print an error message if deserialization fails
            """
            print(f"An error occurred while deserializing: {e}")
            return None
