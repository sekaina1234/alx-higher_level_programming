#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists representing the matrix.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row of the matrix does not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for elem in row:
            result = round(elem / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
