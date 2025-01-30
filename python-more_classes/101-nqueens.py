#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen on the board at position (row, col).
    It checks the row, the upper diagonal, and the lower diagonal for conflicts.
    """
    for i in range(row):
        # Check column conflict
        if board[i][1] == col:
            return False
        # Check upper diagonal conflict
        if board[i][1] - i == col - row:
            return False
        # Check lower diagonal conflict
        if board[i][1] + i == col + row:
            return False
    return True

def solve_nqueens(N, board, row):
    """
    Backtracking method to find all the solutions to the N queens problem.
    The board is represented as a list of (row, col) pairs.
    """
    if row == N:
        print(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board.append([row, col])
            solve_nqueens(N, board, row + 1)
            board.pop()

def nqueens(N):
    """
    Main function to solve the N queens problem by calling the backtracking function.
    """
    board = []
    solve_nqueens(N, board, 0)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)

if __name__ == "__main__":
    main()
