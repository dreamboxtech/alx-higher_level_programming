#!/usr/bin/python3
from add_0 import add

def main():
	a = 1
	b = 2
	res = add(a, b)
	print("{:d} + {:d} = {:d}".format(a, b, res))


if __name__ == 'main':
	main()
