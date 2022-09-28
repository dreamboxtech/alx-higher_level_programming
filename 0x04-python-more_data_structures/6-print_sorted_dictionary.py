#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    return print(
        *[f"{k}: {a_dictionary[key]}" for k in sorted(a_dictionary.keys())],
        sep="\n")
