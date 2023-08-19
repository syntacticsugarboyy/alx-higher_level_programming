#!/usr/bin/python3
'''
    element_at - Returns the index of an element in a list
'''
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    return my_list[idx]
