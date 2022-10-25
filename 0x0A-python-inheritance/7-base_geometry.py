#!/usr/bin/python3
"""Module that has an empty base class BaseGeometry and empty class function
"""


class BaseGeometry:
    """Class that defines a shape
    """
    def area(self):
        """Function that calculates the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Runs an evaluation on value and reponds with appropriate errors"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
