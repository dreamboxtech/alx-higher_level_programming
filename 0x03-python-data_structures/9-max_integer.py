#!/usr/bin/python3

def max_integer(my_list=[]):
    temp = -9e4500
    if my_list:
        for num in my_list:
            if num > temp:
                temp = num
        return temp
    return None


my_list = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))