#!/usr/bin/python3
"""Define MagicClass"""
# import dis
import math


class MagicClass:
    """Circle"""
    def __init__(self, radius=0):
        """Initialize magicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """Calculate area"""
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """Calculate circumference"""
        return 2 * math.pi * self.__radius
# dis.dis(MagicClass)
