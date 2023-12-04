#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Same Class or Inherit from
'''


def is_kind_of_class(obj, a_class):
    '''
        Checks if an object is an instance of, or inherited instance.
    '''
    if isinstance(obj, a_class):
        return True
    return False
