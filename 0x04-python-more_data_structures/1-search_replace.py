#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for idx in my_list:
        if idx == search:
            idx = replace
        new_list.append(idx)
    return new_list
