#!/usr/bin/python3
"""
Contains the class Sqaure
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class with public instance methods area and integer_validator"""
    def __init__(self, size):
        """Constructor sets everything"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Simply returns evaluated area"""
        return self.__size * self.__size
