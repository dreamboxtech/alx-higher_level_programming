#!/usr/bin.python3

def max_integer(my_list=[]):
    temp = -9e4500
    if my_list:
        for num in my_list:
            if num > temp:
                temp = num
        return temp
    return None
