#!/usr/bin/python3
"""Script that takes in a letter & sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""
    values = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"
    body = requests.post(url, values)
    try:
        body.raise_for_status()
        json = body.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print("Not a valid JSON")
