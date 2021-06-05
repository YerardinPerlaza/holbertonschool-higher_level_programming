#!/usr/bin/python3
""" create a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherit from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """overloading the str method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

"""
    @property
    def size(self):
        ""get value of size""
        return self.width

    @size.setter
    def size(self, value):
        ""set the value of size""
        self.width = value
        self.height = value
"""


