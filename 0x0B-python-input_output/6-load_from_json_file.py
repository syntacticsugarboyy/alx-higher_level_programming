#!/usr/bin/python3
'''
    Create object from a JSON file
'''
import json


def load_from_json_file(filename):
    '''
        Creates an Object from a “JSON file”
    '''
    with open(filename, 'r') as file:
        new_obj = json.load(file)
    return new_obj
