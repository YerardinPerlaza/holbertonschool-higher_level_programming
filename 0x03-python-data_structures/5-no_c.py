#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    index = 0
    for i in my_list:
        if i is 'c' or i is 'C':
            my_list[index] = ""
        index += 1
    return "".join(my_list)
