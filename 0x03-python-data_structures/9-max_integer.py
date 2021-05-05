#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    maximum = 0
    for i in my_list:
        if maximum < my_list[i]:
            maximum = my_list[i]
    return (maximum)
