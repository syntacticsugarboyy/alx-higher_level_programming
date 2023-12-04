#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Rectangle
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Inherits from the BaseGeometry class
    '''
    def __init__(self, width, height):
        '''
            Instantiation method
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
