#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL
& displays the body of the response."""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    body = requests.get(url)
    try:
        body.raise_for_status()
        print(body.text)
    except Exception:
        print("Error code: {}".format(body.status_code))
