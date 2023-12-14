#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    And now, the Square!
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        A Square is a rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
            Instantiation
        '''
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        '''
            Returns size
        '''
        return (self.__width)

    @size.setter
    def size(self, value):
        '''
            Validates and sets size
        '''
        self.__width = value
        self.__height = value

    def __str__(self):
        '''
            string representation
        '''
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id, self.x,
                self.y, self.width))
