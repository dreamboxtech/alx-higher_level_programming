#!/usr/bin/python3
"""A a simple example of reading from a file"""


def append_write(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, encoding='utf-8', mode='a') as f:
        f.write(text)
    return len(text)
