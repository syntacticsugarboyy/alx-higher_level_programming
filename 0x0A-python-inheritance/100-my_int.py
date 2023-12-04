#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    My integer
'''


class MyInt(int):
    '''
        Inverts Operators
    '''
    def __eq__(self, value):
        '''
            Overides the equator(== with !=)
        '''
        return self.real != value

    def __ne__(self, value):
        '''
            Overides the negator(!= with ==)
        '''
        return self.real == value
