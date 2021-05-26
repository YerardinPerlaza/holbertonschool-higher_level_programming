#!/usr/bin/python3
'''
prints a text with 2 new lines after
each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    Separate in new lines for ? : or .
    '''
    new = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for letter in text:
        new += letter
        if letter == "." or letter == "?" or letter == ":":
            while new[0] == " ":
                new = new[1:]
            print(new)
            print()
            new = ""
    if len(new) != 0:
        try:
            while new[0] == " ":
                new = new[1:]
        except:
            pass
        print(new, end="")
