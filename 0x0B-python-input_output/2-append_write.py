#!/usr/bin/python3
"""append text to a file"""


def append_write(filename="", text=""):
    """append text to a file with WITH"""

    with open(filename, mode="a", encoding="utf-8") as myfile:
        myfile.write(text)
        return len(text)
