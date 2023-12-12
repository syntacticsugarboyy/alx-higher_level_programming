#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    First Rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''
        A Rectangle is a Base
    '''

    @property
    def width(self):
        '''
            Retrieves width
        '''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''
            Sets and validates width
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''
            Retrieves height
        '''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''
            Sets and validates height
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''
            Retrieves x
        '''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''
            Sets x
        '''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''
            Retrieves y
        '''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''
            Sets and validates y
        '''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Instantiation
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def area(self):
        '''
            Returns the area
        '''
        return (self.__width * self.__height)

    def display(self):
        '''
            Prints the rectangle
        '''
        for height in range(self.__height):
            for width in range(self.__width):
                print('#', end='')
            print('')
