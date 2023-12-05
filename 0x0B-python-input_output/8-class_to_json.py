#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Class to JSON
'''
import json


def class_to_json(obj):
    '''
       Converts class to JSON
    '''
    return (obj.__dict__)
