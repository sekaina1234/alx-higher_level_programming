#!/usr/bin/python3
"""N queens."""


import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while j >= 0 and i < len(board):
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(n):
    """Solve the N queens problem."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve_util(board, col):
        """Utility function to solve the N queens problem."""
        # Base case: If all queens are placed
        if col == n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True

        # Consider this column and try placing a queen in all rows
        for row in range(n):
            if is_safe(board, row, col):
                # Place the queen in the current position
                board[row][col] = 1

                # Recur to place the rest of the queens
                solve_util(board, col + 1)

                # Backtrack and remove the queen from the current position
                board[row][col] = 0

    solve_util(board, 0)

    return solutions


if __name__ == "__main__":
    # Get the number of queens from the command line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    solutions = solve_nqueens(n)

    # Print the solutions
    for solution in solutions:
        print(solution)
