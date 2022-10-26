#!/usr/bin/python3
""" a class Student that defines a student by:"""


class Student:
    """ a class Student that defines a student by:
        Public instance attributes:
        first_name
        last_name
        age"""
    def __init__(self, first_name, last_name, age):
        """Initializes Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation
        of a Student instance"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
