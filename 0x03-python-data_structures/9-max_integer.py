#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    largest = my_list[0]
    for num in range(1, len(my_list)):
        if largest < my_list[num]:
            largest = my_list[num]
    return largest
