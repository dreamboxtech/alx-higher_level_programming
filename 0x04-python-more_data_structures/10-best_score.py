#!/usr/bin/python3

def best_score(a_dictionary):
    return [None if not (a_dictionary or None) else
            sorted(a_dictionary, key=a_dictionary.get)[-1]][0]
