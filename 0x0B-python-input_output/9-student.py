#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Student to JSON
'''


class Student:
    '''
        Student to JSON
    '''
    def __init__(self, first_name, last_name, age):
        '''
            Instantiation
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
            Dictionary repr of Student
        '''
        return (self.__dict__)
