#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Rectangle
    Author: syntacticsugrboyy
'''


class Rectangle:
    '''
        Rectangle: A class defining a Rectangle
    '''
    @property
    def width(self):
        '''
            Retrieves the private instance attribute width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Sets the width attribute with value

            Args:
                self: Class parameter
                value: value to be set

            Raises:
                TypeError if value is not an integer
                ValueError if value is < 0
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''
            Retrieves the private instance attribute height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Sets the height attribute with value

            Args:
                self: Class property
                value: value to be set

            Raises:
                TypeError if value is not an int
                ValueError if value < 0
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def __init__(self, width=0, height=0):
        '''
            Creates a new instance of Rectangle

            Args:
                self: Class property
                width: width of new rectangle
                height: height of new rectangle
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width

    def area(self):
        '''
            Calculates the area of the Rectangle
        '''
        return (self.__height * self.__width)

    def perimeter(self):
        '''
            Calculates the perimeter of the Rectangle
        '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
