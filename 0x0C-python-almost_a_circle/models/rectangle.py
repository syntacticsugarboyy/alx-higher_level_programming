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
            Sets width
        '''
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
            Sets height
        '''
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
            Sets y
        '''
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
