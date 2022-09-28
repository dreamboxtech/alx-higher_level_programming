#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    return print(*[f"{k}: {a_dictionary[k]}" for k in sorted(a_dictionary.keys())],
                 sep="\n", end='')

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
# a_dictionary = {"one":'two', 'three':'one', 'two':'three', "a": {"zaba": 0, "abba": 1}}
print_sorted_dictionary(a_dictionary)
