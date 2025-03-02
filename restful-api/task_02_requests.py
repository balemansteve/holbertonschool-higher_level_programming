#!/usr/bin/python3
"""
This script fetches data from a given URL using the requests library
and prints the HTTP status code of the response.
"""
import requests


url = "http://www.google.com"

def fetch_and_print_posts():
    """
    Fetch data from the specified URL and print the HTTP status code.
    Args:
        None
    Return:
        None
    """
    response = requests.get(url)
    if response.status_code == 200:
        print("Status Code:", response.status_code)

fetch_and_print_posts()
