#!/usr/bin/python3
'''
    Student to JSON
'''


class Student:
    '''
        a class named Student
    '''
    def __init__(self, first_name, last_name, age):
        '''
            Initializes a Student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            Grabs Student details
        '''
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if
                hasattr(self, attr)}
