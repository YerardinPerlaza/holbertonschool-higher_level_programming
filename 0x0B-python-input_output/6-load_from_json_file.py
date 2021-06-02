#!/usr/bin/python3
"""create and object from a json file"""
import json


def load_from_json_file(filename):
    """create from json"""
    with open(filename, encoding="utf-8") as myfile:
        my_obj = json.load(myfile)

    return my_obj
