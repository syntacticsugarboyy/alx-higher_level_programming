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

        Returns TypeError if size is not an int
        Returns ValueError if size < 0
    '''
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                ValueError('size must be >= 0')
        else:
            TypeError('size must be an integer')

    def area(self):
        return (self.__size ** 2)
