#!/usr/bin/python3
"""A a simple example of reading from a file"""
import json


def load_from_json_file(filename):
    """  a function that creates an Object
    from a “JSON file”:"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            obj = json.loads(line)
    return obj
