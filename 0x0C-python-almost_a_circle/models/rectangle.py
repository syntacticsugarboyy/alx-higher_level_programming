#!/usr/bin/python3
'''
    First Rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''
        A class Rectangle that inherits from Base
    '''
    @property
    def width(self):
        '''
            Private Getter for width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Sets the width property
        '''
        self.all_checks('width', value)
        self.__width = value

    @property
    def height(self):
        '''
            Private Getter for height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Sets the height property
        '''
        self.all_checks('height', value)
        self.__height = value

    @property
    def x(self):
        '''
            Private Getter for x
        '''
        return self.__x

    def x(self, value):
        '''
            Sets the x property
        '''
        self.all_checks('x', value)
        self.__x = value

    @property
    def y(self):
        '''
            Private Getter for y
        '''
        return self.__y

    def y(self, value):
        '''
            Sets the property for y
        '''
        self.all_checks('y', value)
        self.__y = value

    def all_checks(self, attribute, value):
        '''
            unittest
        '''
        self.type_int_check(attribute, value)
        if attribute == 'x' or attribute == 'y':
            self.nagative_check(attribute, value)
        else:
            self.zero_and_negative_check(attribute, value)

    def attribute_check(self, attribute):
        '''
            Attribute check
        '''
        if type(attribute) is not str:
            raise TypeError('attribute mnust be of type str')

    def zero_and_negative_check(self, attribute, value):
        '''
            Zero and -ve check
        '''
        self.attribute_check(attribute)
        if value <= 0:
            raise ValueError('{} must be > 0'.format(attribute))

    def negative_check(self, attribute, value):
        '''
            Negative check
        '''
        self.attribute_check(attribute)
        if value < 0:
            raise ValueError('{} must be >= 0'.format(attribute))

    def type_int_check(attribute, self, value):
        '''
             Checks type for int
        '''
        self.attribute_check(attribute)
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(attribute))

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Initializes a Rectangle
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def area(self):
        '''
            Calculates area
        '''
        return (self.__width * self.__height)

    def display(self):
        '''
            Prints the rectangle
        '''
        rect = ''
        for y in range(self.__y):
            rect += '\n'
        for height in range(self.__height):
            rect += (' ' * self.__x) + ('#' * self.__width)
            if height != (self.__height - 1):
                rect += '\n'
            print(rect)

    def __str__(self):
        string = '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'
        return (string.format(self.id, self.__x, self.__y, self.__width,
                self.__height))

    def update(self, *args, **kwargs):
        '''
            Assigns arguments to attributes
        '''
        if args and len(args) != 0:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
        elif kwargs:
            valid_attributes = ['id', 'width', 'height', 'x', 'y']
            for key, value in kwargs.items():
                if key in valid_attributes:
                    exec('self.{} = {}'.format(key, value))

    def to_dictionary(self):
        '''
            Returns a dictionary
        '''
        return {
                'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height':self.__height,
                'width': self.__width
                }
