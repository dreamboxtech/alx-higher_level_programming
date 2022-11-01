#!/usr/bin/python3
"""
A simple base file

"""


class Base:
    """This is the base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """The default constructor for the base class
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
