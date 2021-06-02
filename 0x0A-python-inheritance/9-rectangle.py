#!/usr/bin/python3
""" Geometry class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Implement rectangle"""
    def __init__(self, width, height):
        """Initialize class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """calculate area"""
        return (self.__width * self.__height)

    def __str__(self):
        """magic method str"""
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
