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

    def to_json(self, attrs=None):
        '''
            Dictionary repr of Student
        '''
        if isinstance(attrs, list) and all (isinstance(elem, str) for elem in attrs):
            return ({k: getattr(self, k) for k in attrs if hasattr(self, k)})
        return (self.__dict__)

    def reload_from_json(self, json):
        '''
            Replaces attributes of student
        '''
        for key, value in json.items():
            setattr(self, key, value)
