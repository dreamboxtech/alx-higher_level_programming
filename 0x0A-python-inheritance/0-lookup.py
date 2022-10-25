#!/usr/bin/python3
"""Function that returns attributes and 
methods in a class
"""


def lookup(obj):
    """This functions returns methods and 
    attributes of an object.
    Args:
        obj - the target object
    """
    
    return dir(obj)
