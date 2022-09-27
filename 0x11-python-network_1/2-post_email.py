#!/usr/bin/python3
"""Script that takes in a URL & an email
sends a POST request to the URL with the email as a parameter
& displays the body of the response (decoded in utf-8)"""


import urllib.request
import sys
import urllib.parse
if __name__ == '__main__':

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
