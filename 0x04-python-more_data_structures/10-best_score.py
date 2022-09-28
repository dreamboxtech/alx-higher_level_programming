#!/usr/bin/python3

def best_score(a_dictionary):
    return [None if not (a_dictionary or None) else max(a_dictionary)][0]
