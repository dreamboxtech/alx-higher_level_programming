#!/usr/bin/python3
"""A a simple example of reading from a file"""
import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of
    an object (string):"""
    return json.dumps(my_obj)
