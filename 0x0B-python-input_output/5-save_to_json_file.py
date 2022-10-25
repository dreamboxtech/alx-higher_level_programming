#!/usr/bin/python3
"""A a simple example of reading from a file"""
import json


def save_to_json_file(my_obj, filename):
    """  a function that writes an Object to a text file, using a
    JSON representation:"""
    with open(filename, encoding='utf-8', mode='w') as f:
        f.write(json.dumps(my_obj))
