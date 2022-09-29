#!/usr/bin/python3
def roman_to_int(roman_string):

    if (type(roman_string) != str) or (roman_string is None):
        return 0
    pairs = {"I": 1, "V": 5, "X": 10,
             "L": 50, "C": 100, "D": 500, "M": 1000}

    c = [pairs[roman_string[i]] for i in range(len(roman_string))]
    num = c[0]
    for i in range(len(c)-1):
        if c[i] >= c[i+1]:
            num += c[i+1]
        else:
            num += (c[i+1] - c[i] - c[i])

    return num
