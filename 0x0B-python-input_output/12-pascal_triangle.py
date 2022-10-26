#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [[1], [1, 1]]
    angle = [1, 1]
    for i in range(2, n):
        angle = [1] + [sum(values) for values in zip(angle[1:], angle)] + [1]
        triangle.append(angle)
    return triangle
