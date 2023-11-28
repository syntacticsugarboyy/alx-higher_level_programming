#!/usr/bin/python3
'''
    Low memory cost
'''


class LockedClass:
    '''
        Prevents users from creating new instance attributes
        except firstname
    '''
    __slots__ = ['first_name']
