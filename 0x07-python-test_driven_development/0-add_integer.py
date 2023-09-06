#!/usr/bin/pyhton3
# -*- coding: utf-8 -*-
'''
    Adds Integers
    Author: syntactic_sugarboyy
'''


# 0-add_integer.txt
def add_integer(a, b=98):
    '''
        add_integer: adds integers

        Args:
            a: first integer
            b: second integer(default 98)

        Raises:
            TypeError if a or b are not integers
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)


'''if __name__ == '__main__':
    import doctest
    doctest.testfile('0-add_integer.txt')'''
