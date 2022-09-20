#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number > 0:
        last = number%10
    if number < 0:
        last = -1 * (abs(number)%10)
    print("{}".format(last), end='')
    return last
