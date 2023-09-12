#!/usr/bin/python3
'''
    BaseGeometry
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
        A Square is a Rectangle
    '''
    def __init__(self, size):
        '''
            Initializes a rectangle
        '''
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()