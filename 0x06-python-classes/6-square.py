#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Square
    Author: syntactic_sugarboyy
'''


class Square:
    '''
        Creates a class Square
    '''
    '''
        Retrieves an attribute size
    '''
    @property
    def size(self):
        return self.__size

    '''
        Sets a value to the size property
        
        Args:
            value: value to be set

        Raises TypeError if value is not an integer
        Raises ValueError if value < 0
    '''
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    '''
        Retrieves a position
    '''
    @property
    def position(self):
        return self.__position

    '''
        Sets the position

        Args:
            value: value to be set

        Raises TypeError if value is not a tuple of 2 positive integers
    '''
    def position(self, value):
        if not isinstance(value, tuple) or value > 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    '''
        Creates an instance

        Args:
            size: size of square
            position: Position of square
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    '''
        Returns the area of the square
    '''
    def area(self):
        return (self.__size ** 2)

    '''
        Prints the square to stdout
    '''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for pos in range(self.__position[1], 0, -1):
                    print()
            for length in range(self.__size):
                for pos in range(self.__position[0]):
                    print('_'.format(self.__position[0]), end='')
                for length in range(self.__size):
                    print('#', end='')
                print()
