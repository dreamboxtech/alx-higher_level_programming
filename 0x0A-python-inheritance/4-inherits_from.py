#!/usr/bin/python3
"""Module that contains a class MyList that inherits from list
"""


def inherits_from(obj, a_class):
    """Function that returns True or False based on type"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
