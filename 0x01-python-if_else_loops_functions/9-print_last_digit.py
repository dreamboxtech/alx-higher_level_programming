#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last = -1 * (abs(number) % 10)
    last = number % 10
    print("{}".format(last), end='')
    return last
