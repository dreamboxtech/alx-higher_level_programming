#!/usr/bin/python3
"""Unit Testing..."""


def add_integer(a, b=98):
    """Basic add function"""
    if type(a) not in [float, int]:
        raise TypeError:
            print("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError:
            print("b must be an integer")
    a = int(a)
    b = int(b)
    return (a+b)
