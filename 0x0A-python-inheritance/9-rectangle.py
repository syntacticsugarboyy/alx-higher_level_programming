#!/usr/bin/python3
'''
    BaseGeometry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        ''' prints the rectangle '''
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
