#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class with public instance methods area and integer_validator"""
    def __init__(self, width, height):
        """Constructor sets everything"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Simply returns evaluated area"""
        return self.__width * self.__height

    def __str__(self):
        """Outputs the result for the class"""
        return f"[Rectangle] {self.__width}/{self.__height}"
