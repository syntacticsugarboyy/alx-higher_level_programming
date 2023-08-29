#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' Square
    Author: syntactic_sugarboyy
'''


class Square:
    '''
        Creates a class called Square
        Args:
            self: class
            size: size of square
        Raises TypeError if size is not an integer
        Raises ValueError if size is less than 0
    '''
    def __init__(self, size=0):
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
