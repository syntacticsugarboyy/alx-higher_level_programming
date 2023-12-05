#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    To JSON string
'''
import json


def to_json_string(my_obj):
    '''
        Converts an object to JSON format
    '''
    return (json.dumps(my_obj))
