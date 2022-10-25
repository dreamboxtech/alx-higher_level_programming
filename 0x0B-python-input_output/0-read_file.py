#!/usr/bin/python3
"""A a simple example of reading from a file"""


def read_file(filename=""):
    """This simple function accepts file name as arguement and prints
    out the content of the file"""
    with open(filename, encoding='utf-8') as f:
        print(f.readlines(), end='')
