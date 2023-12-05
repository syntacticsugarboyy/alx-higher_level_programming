#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
     From JSON string to Object
'''
import json


def from_json_string(my_str):
    '''
        Converts JSON string to Python datatype
    '''
    return (json.loads(my_str))
