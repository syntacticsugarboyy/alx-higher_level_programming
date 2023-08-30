#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Square
    Author: syntactic_sugarboyy
'''


class Square:
    '''
        Creates a class named Square

        Args:
            self: class
    '''
    '''
        Retrieves the size property
    '''
    @property
    def size(self):
        return self.__size

    '''
        Sets the value of the size property when called

        Args:
            value: value we want to set as size

        Raises TypeError if value is not an int
        Raises ValueError if value < 0
    '''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    '''
        Creates an instance

        Args:
            size: size of square

        Raises TypeError if value is not an int
        Raises ValueError if value < 0
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    '''
        Calculates the area of the square
    '''
    def area(self):
        return (self.__size ** 2)

    '''
        Prints the Square to stdout
    '''
    def my_print(self):
        if self.__size == 0:
            print()
        for length in range(self.__size):
            for length in range(self.__size):
                print('#', end='')
            print()
