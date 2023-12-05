#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Append to a file
'''


def append_write(filename="", text=""):
    '''
        Appends a string to the end of a text file
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
