#!/usr/bin/python3
"""Script that takes in a URL,sends a request to
the URL and displays the body of the response"""

if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys

    body = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(body) as res:
            print(res.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
