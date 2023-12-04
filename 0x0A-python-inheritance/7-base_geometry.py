#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
     Improve Geometry
'''


class BaseGeometry:
    '''
        Shapes
    '''
    def area(self):
        '''
            Raises an exception
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
            Indicates Value
        '''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        self.name = value
