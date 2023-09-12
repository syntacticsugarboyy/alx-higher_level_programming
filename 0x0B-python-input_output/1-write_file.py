#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Writes a string to a file
'''


def write_file(filename="", text=""):
    ''' writes text into a file '''
    if not filename:
        return
    with open('filename', 'w', encoding='utf-8') as file:
        return file.write(text)
