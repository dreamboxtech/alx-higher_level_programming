#!/usr/bin/python3
import sys


def run():
    args = sys.argv
    return sum(map(int, args[1:]))


if __name__ == "__main__":
    print(run())
