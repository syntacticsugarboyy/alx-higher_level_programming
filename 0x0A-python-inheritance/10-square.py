#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Square #1
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
        A Square is a Rectangle
    '''
    def __init__(self, size):
        '''
            Instantiation
        '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
