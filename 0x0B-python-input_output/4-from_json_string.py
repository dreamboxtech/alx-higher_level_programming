#!/usr/bin/python3
"""A a simple example of reading from a file"""
import json


def from_json_string(my_str):
    """ a function that returns an object (Python data structure)
    represented by a JSON string:"""
    return json.loads(my_str)
