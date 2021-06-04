#!/usr/bin/python3
"""create a class rectangle that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """create class rectangle
    inherit from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize width, height, x and y"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(sel, value):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(sel, value):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(sel, value):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(sel, value):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """display the rectangle with #"""
        rectangle = ""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            rectangle += (" " * self.__x) + ("#" * self.__width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """ overriding the str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                                                       self.__width, self.__height)

    def update(self, *args):
        """assign an argument to each attribute"""
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            return
