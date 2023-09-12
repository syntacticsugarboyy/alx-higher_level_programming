#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    is same class?
'''


def is_same_class(obj, a_class):
    '''
        Checks if an object is an instance of a class

        Args:
            obj: object
            a_class: superclass

        Returns:
            True if yes
            False if otherwise
    '''
    return type(obj) is a_class
