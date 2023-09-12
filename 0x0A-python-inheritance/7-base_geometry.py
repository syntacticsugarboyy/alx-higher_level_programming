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
