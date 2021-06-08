#!/usr/bin/python3
""" create a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherit from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """get value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """overloading the str method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """return the dictionary representation"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
