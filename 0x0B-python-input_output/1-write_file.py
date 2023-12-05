#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Write to a file
'''


def write_file(filename="", text=""):
    '''
        Writes a string to a text file
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
