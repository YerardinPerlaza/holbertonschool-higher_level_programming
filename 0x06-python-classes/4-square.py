#!/usr/bin/python3
"""Class square"""


class Square:
    """Initialize class square"""
    def __init__(self, size=0):
        self.__size = size

    # Property
    @property
    def size(self):
        """Initialize object with size"""
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
        """Size and errors"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2
