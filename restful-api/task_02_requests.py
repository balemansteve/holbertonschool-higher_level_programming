#!/usr/bin/python3
"""
This script fetches data from a given URL using the requests library
and prints the HTTP status code of the response.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch data from the specified URL and print the HTTP status code.
    Args:
        None
    Return:
        None
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch data from the specified URL and save it to a CSV file.
    Args:
        None
    Return:
        None
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        post_list = []
        for post in posts:
            post_list.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body'],
            })
        with open("posts.csv", 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(post_list)

fetch_and_print_posts()
fetch_and_save_posts()
