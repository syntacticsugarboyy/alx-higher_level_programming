#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Simple Rectangle
'''


class Rectangle:
    '''
        Rectangle
    '''
    @property
    def width(self):
        '''
            Gets the width property
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Sets the width property to value
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''
            Gets the height property
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Sets the height property
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def __init__(self, width=0, height=0):
        '''
            Instantiation attribute
        '''
        self.__height = height
        self.__width = width

    def area(self):
        '''
            Returns the area of the Rectangle
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''
            Returns the perimeter of the Rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        string = ''
        if self.__width == 0 or self.__height == 0:
            return ('')
        for height in range(self.__height):
            for width in range(self.__width):
                string += '#'
            string += '\n'
        return string[:-1]

    def __repr__(self):
        '''
            eval()
        '''
        return ('Rectangle({:d}{:d})'.format(self.__width, self.__height))

    def __del__(self):
        '''
            Deletes an instance
        '''
        print('Bye rectangle...')
