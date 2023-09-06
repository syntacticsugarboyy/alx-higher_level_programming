#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    print_square: prints a square
'''


def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    if size == 0:
        print()
    else:
        for square in range(size):
            for square in range(size):
                print('#', end='')
            print()
