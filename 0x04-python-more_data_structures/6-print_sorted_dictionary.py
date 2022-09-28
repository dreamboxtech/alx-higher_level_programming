#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    return print(*[f"{k}: {v}" for k, v in sorted(a_dictionary.items())],
                 sep="\n", end='')
