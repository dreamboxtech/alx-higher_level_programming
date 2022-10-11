#!/usr/bin/python3
"""An empty 'class Square' here"""


class Square:
    """ A square is a four-sided shape"""
    def __init__(self, size=0):
        """Contructor set up goes here..."""

        if isinstance(self.__size, int):
            if self.__size < 0:
                raise Exception("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer"):
