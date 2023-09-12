#!/usr/bin/python3
'''
    BaseGeometry
'''


class BaseGeometry:
    '''
        A parent Class named BaseGeometry
    '''
    def area(self):
        '''
            Raises:
                Exception
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
            Validates value
        '''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        self.name = value

class Rectangle(BaseGeometry):
    '''
        A Rectangle is a Geometric object
    '''
    def __init__(self, width, height):
        '''
            Initializes a rectangle
        '''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
