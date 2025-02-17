#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to XML and save it to a file
    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The name of the file to save the XML data
    Returns:
        bool: Always returns True after saving
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)
    return True

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a dictionary
    Args:
        filename (str): The file containing XML data
    Returns:
        dict: The deserialized dictionary, or None if parsing fails
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {child.tag: child.text for child in root}
        return dictionary
    except ET.ParseError:
        return False
