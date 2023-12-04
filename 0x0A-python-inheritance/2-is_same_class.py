#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Exact Same Object
'''


def is_same_class(obj, a_class):
    '''
        Checks if an object is an instance of the specifies class
    '''
    if type(obj) == a_class:
        return True
    return False
