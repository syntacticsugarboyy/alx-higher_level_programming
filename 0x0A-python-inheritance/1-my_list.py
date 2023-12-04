#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    My List
'''


class MyList(list):
    '''
        Inherits stuff from list
    '''
    def print_sorted(self):
        '''
            Prints a list in ascending sort
        '''
        print(sorted(self))
