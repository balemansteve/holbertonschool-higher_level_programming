#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n 
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [last_row[j] + last_row[j]
                for j in range(len(last_row))]
        row.append(1)
        triangle.append(row)
    return triangle
