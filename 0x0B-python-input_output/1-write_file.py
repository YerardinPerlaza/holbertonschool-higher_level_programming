#!/usr/bin/python3
"""write a file"""


def write_file(filename="", text=""):
    """write a file with WITH"""

    with open(filename, mode="w", encoding="utf-8") as myfile:
        myfile.write(text)
        return len(text)
