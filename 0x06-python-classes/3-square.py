#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Square
    Author: syntactic_sugarboyy
'''


class Square:
    '''
        Creates a class Square
            Args:
                self: class
                size: size of Square
            Raises TypeError if size is not an integer
            Raises ValueError if size is < 0
    '''
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        '''
            Returns the area of the Square
        '''
        return (self.__size ** 2)
