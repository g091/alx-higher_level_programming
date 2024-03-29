#!/usr/bin/python3
"""Script that takes in a URL, sends a request
    to the it & displays the value of the X-Request-Id
    variable found in the header of the response"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()["X-Request-Id"]
        print(header)
