#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Read file
'''


def read_file(filename=""):
    '''
        Reads a text file
    '''
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
