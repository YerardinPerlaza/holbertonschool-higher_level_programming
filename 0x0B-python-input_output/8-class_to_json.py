#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """the dict representation of a class"""
    return (getattr(obj, "__dict__"))
