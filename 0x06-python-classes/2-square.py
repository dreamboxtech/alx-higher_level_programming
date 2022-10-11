#!/usr/bin/python3
"""An empty 'class Square' here"""


class Square:
    """ A square is a four-sided shape"""
    def __init__(self, size=0):
        """Contructor set up goes here..."""
        self.__size = size
        try:
            int(self.__size)
        except TypeError:
            print("size must be an integer")
        if self.__size < 0:
            raise Exception:
                print("size must be >= 0")
