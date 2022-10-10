#!/usr/bin/python3

def safe_print_division(a, b):
    res = int
    try:
        res = a/b
    except (TypeError, ValueError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
