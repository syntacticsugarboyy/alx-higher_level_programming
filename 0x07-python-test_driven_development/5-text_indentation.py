#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Text Indentation
    Author: syntacticsugarboyy
'''

def text_indentation(text):
    '''
        Prints a text and some indentation
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
	start = 0
    for i in range(len(text)):

        if (ord(text[i]) == ord(".") or ord(text[i]) == ord("?")
            or ord(text[i]) == ord(":")):
            none_found = False
            string_to_print = text[start:i + 1].strip()
            print(f"{string_to_print}\n\n", end="")
            if (i + 1) <= (len(text) - 1):
                start = i + 1
    if none_found:
        print(text.strip(), end="")
    elif start != (len(text) - 1):
        print(text[start:len(text)].strip(), end="")
