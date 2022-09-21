#!/usr/bin/python3
def remove_char_at(str, n):
    return str.replace(str[str.index(str[n])], "")
