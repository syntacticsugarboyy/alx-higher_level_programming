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
