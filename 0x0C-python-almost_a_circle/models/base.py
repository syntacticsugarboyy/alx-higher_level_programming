#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Base Class
'''


class Base:
    '''
        Base Class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
            Instantiation
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
