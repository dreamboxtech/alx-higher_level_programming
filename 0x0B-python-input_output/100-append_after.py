#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
     after each line containing a specific stringe.
    """
    with open(filename, mode='r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if search_string in line:
                line = line + new_string
            f.writelines(line)
