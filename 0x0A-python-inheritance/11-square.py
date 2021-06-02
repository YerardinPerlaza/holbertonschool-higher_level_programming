#!/usr/bin/python3
"""Implementing a Geometry class"""


class BaseGeometry:
    """Class geometry"""
    def area(self):
        """Calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Implement rectangle"""
    def __init__(self, width, height):
        """Initialize rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """calculate area"""
        return (self.__width * self.__height)

    def __str__(self):
        """magic method"""
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))


class Square(Rectangle):
    """ Implement class Square"""
    def __init__(self, size):
        """Initialize class square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculate area"""
        return (self.__size ** 2)
