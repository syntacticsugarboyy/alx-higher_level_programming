#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Create object from a JSON file
'''
import json


def load_from_json_file(filename):
    '''
        Creates an Object from a “JSON file”
    '''
    with open(filename) as file:
        return (json.load(file))
