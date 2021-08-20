#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    returns the peak of a list
    """
    if list_of_integers != []:
        list_of_integers.sort()
        return list_of_integers[-1]
