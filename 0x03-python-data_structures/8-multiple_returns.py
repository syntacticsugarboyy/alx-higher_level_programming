#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
        return length, first
    first = sentence[0]
    return length, first

