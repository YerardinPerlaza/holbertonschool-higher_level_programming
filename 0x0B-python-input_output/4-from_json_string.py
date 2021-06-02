#!/usr/bin/python3
"""return an object for json representation"""
import json


def from_json_string(my_str):
    """json representation"""
    return json.loads(my_str)
