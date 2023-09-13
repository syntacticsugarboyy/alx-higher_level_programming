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

    def to_json(self):
        '''
            Grabs Student details
        '''
        return self.__dict__
