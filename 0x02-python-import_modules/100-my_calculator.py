#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def run():
    len_args = len(sys.argv[1:])
    args = sys.argv[1:]
    if len_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if not any(op in args for op in "+-*/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    op = args[1]
    a = int(args[0])
    b = int(args[2])

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    run()
