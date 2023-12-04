#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Only sub class of
'''


def inherits_from(obj, a_class):
    '''
        Checks if an object is an inheritance.
    '''
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
