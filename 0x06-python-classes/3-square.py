#!/usr/bin/python3
"""Class square"""


class Square:
    """Initialize class square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Calculate area of a square"""
        size = self.__size
        return size * size
