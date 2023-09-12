#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    MyList
    Inherits from list
'''


class MyList(list):
    '''
        SuperClass
    '''
    def print_sorted(self):
        '''
            Prints a list in ascending order
        '''
        sorted_list = super().copy()
        sorted_list.sort()
        print(sorted_list)
