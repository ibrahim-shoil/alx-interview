#!/usr/bin/python3
"""
A module that contains the function pascal_triangle to generate Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth level.

    Args:
        n (int): The number of levels of Pascal's triangle to generate.

    Returns:
        list of lists: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # The first level of Pascal's triangle is always [1]
    
    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)
    
    return triangle

