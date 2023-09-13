#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Reads a file
'''


def read_file(filename=""):
    '''
        Reads a file
    '''
    with open('filename', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
