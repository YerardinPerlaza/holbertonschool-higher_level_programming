#!/usr/bin/python3
"""writes and object to a text file using json"""
import json


def save_to_json_file(my_obj, filename):
    """save to json"""
    with open(filename, mode="w") as myfile:
        json.dump(my_obj, myfile)
