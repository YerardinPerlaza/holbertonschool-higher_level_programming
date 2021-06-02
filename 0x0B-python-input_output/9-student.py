#!/usr/bin/python3
"""create a class to define student"""


class Student:
    """create a class"""
    def __init__(self, first_name, last_name, age):
        """Initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retieves a dictionary representation"""
        return self.__dict__
