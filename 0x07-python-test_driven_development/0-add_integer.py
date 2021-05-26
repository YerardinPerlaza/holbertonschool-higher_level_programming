#!/usr/bin/python3
'''
Add two integer
type:
int / float
'''


def add_integer(a, b=98):
    '''
    Add two integers
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)
