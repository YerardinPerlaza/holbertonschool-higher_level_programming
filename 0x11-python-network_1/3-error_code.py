#!/usr/bin/python3
"""cript that takes in a URL, sends a request to the URL and displays the body of the response"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as request:
            data = request.read()
            print(data.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
