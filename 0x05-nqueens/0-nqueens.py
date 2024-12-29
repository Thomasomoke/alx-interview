#!/usr/bin/python3
import sys


def print_solution(board):
    """Print a solution"""
    print([[i, board[i]] for i in range(len(board))])


def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col)"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, board, row):
    """Solve N Queens using backtracking"""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, board, row + 1)
            board[row] = -1  # Reset position


def main():
    """Main function to handle input and solve the N Queens problem"""
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

    board = [-1] * n  # Initialize board with -1, meaning no queen is placed
    solve_nqueens(n, board, 0)


if __name__ == "__main__":
    main()
