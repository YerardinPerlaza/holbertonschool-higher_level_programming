#!/usr/bin/python3
''' Write a class MyList that inherits from list '''


class MyList(list):
    ''' prints the list, but sorted '''
    def print_sorted(self):
        ''' prints the list, but sorted '''
        print(sorted(self))
