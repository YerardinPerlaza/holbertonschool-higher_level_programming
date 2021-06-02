#!/usr/bin/python3
"""read a file"""


def read_file(filename=""):
    """read a file with WITH"""

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read())
