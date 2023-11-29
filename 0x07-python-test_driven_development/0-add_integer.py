#!/usr/bin/python3
# -*- coding: utf-8 -*-
import doctest
doctest.testfile('tests/0-add_integer.txt')
'''
    Integers addition
'''


def add_integer(a, b=98):
    '''
        A function that adds two integers
    '''
    if not isinstance (a, (int, float)):
        raise TypeError('a must be an integer')

    elif not isinstance (b, (int, float)):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
