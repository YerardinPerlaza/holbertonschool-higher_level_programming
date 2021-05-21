#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """initialize rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """string representation of rectangle"""
        symbol = str(self.print_symbol)
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += symbol * self.__width + '\n'
        rectangle += symbol * self.__width
        return rectangle

    def __repr__(self):
        """repr representation of rectangle to machine"""
        w = str(self.__width)
        h = str(self.__height)
        rectangle = "Rectangle(" + w + ", " + h + ")"
        return rectangle

    def __del__(self):
        """delete rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
