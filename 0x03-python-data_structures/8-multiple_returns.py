#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        new = (0, None)
    else:
        new = (len(sentence), sentence[0])
    return (new)
