#!/usr/bin/python3
'''
write a function that
prints a square with
the character #
'''


def print_square(size):
    '''
    print square
    '''
    square = ""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        square += "#" * size + "\n"
    print(square, end="")
