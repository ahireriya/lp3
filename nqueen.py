def solveNQueens(n: int, first_queen_col: int):
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "Q"

    backtrack(1)  # Start with the second row
    return res

if __name__ == "__main__":
    n = 8
    first_queen_col = 1
    board = solveNQueens(n, first_queen_col)[0]
    for row in board:
        print(" ".join(row))







def is_safe(board, row, col, n):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, n):
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place queen

            if solve_nqueens(board, col + 1, n):
                return True

            board[i][col] = 0  # Backtrack

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

def nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_nqueens(board, 0, n):
        print_board(board)
    else:
        print("No solution exists")
"""
# Example usage
n = 4
nqueens(n)
Explanation
is_safe: Checks if placing a queen at (row, col) would result in a conflict. It verifies:
The row on the left side.
The upper-left diagonal.
The lower-left diagonal.
solve_nqueens: Tries to place queens column by column and backtracks if necessary.
nqueens: Initializes the board and starts solving the problem, printing the solution if one exists.
This will output one valid solution for an 
𝑛
×
𝑛
n×n board if it exists."""
































""""Here's a breakdown of the N-Queens code and an example to help illustrate how it works.

Code Explanation
The solveNQueens function solves the N-Queens problem, where the goal is to place n queens on an n x n chessboard such that no two queens threaten each other. This version takes two inputs:

n: the size of the board (number of rows/columns).
first_queen_col: the column position for the first queen in the first row.
The function uses backtracking to find valid arrangements for the queens.

python

Copy code
def solveNQueens(n: int, first_queen_col: int):
Defines the function solveNQueens, which takes the size of the board n and the initial column first_queen_col for the queen in the first row.
python

Copy code
    col = set()
    posDiag = set()
    negDiag = set()
Initializes three sets to keep track of where queens are already placed:
col: Stores the columns that currently have queens.
posDiag: Stores positive diagonals (difference row + col) with queens.
negDiag: Stores negative diagonals (difference row - col) with queens.
python

Copy code
    res = []
    board = [["."] * n for _ in range(n)]
res: Stores valid board configurations.
board: Initializes an n x n board with all cells set to "." (empty).
python

Copy code
    def backtrack(r):
Defines the nested function backtrack, which attempts to place a queen in each row r recursively.
python

Copy code
        if r == n:
            res.append(["".join(row) for row in board])
            return
Base case: If r == n (all rows are filled), it means we have a valid board configuration. The current board state is added to res.
python

Copy code
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
For each column c in row r, it checks if placing a queen is valid:
Skips c if it’s already in col, posDiag, or negDiag, meaning the column or diagonal is occupied.
python

Copy code
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"
Marks the column, positive diagonal, and negative diagonal as occupied by adding them to col, posDiag, and negDiag.
Places a queen ("Q") at position (r, c) on the board.
python

Copy code
            backtrack(r + 1)
Recursively calls backtrack to place a queen in the next row (r + 1).
python

Copy code
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."
Backtracks by removing the queen from (r, c), resetting the column and diagonals, allowing other configurations to be explored.
python

Copy code
    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "Q"
Places the first queen at the specified first_queen_col in the first row (row 0), marking its column and diagonals.
python

Copy code
    backtrack(1)
Starts the recursive search from row 1 since row 0 is already occupied by the initial queen.
python

Copy code
    return res
Returns the list of valid configurations found."""
