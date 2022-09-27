#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL
& displays the value of the variable X-Request-Id in the response header"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    body = requests.get(url)
    print(body.headers.get('X-Request-Id'))
