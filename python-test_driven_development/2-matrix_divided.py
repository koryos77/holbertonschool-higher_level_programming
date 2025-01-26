#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides matrix elements.

The function ensures that the matrix is a list of lists of integers or floats,
and that the divisor is a non-zero number. It raises appropriate exceptions
for invalid inputs.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Number to divide by.

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    
    if not all(isinstance(elements, (int, float))
               for row in matrix for elements in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
