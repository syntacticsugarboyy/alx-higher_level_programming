#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Writes a string to a file
'''


def write_file(filename="", text=""):
    ''' writes text into a file '''
    with open('filename', 'w', encoding='utf-8') as file:
        return file.write(text)
