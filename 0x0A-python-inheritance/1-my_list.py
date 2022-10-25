#!/usr/bin/python3
"""class that inherits from list class and has a method print_sorted in it
    object
"""

class MyList(list):
    """class that inherits from list class and has a method print_sorted in it
    object
    """

    def print_sorted(self):
        """Method that returns sorted list in ascending order, will use list method, sorted
        """
        print(sorted(self))
