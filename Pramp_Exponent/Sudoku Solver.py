from typing import List

"""
Problem Name: Sudoku Solver

Problem URL: 

Problem Section: Backtracking

Problem Statement:
Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable. If so, the function will returns true. Otherwise (i.e. there is no valid solution to the given sudoku board), returns false.

In sudoku, the objective is to fill a 9x9 board with digits so that each column, each row, and each of the nine 3x3 sub-boards that compose the board contains all of the digits from 1 to 9. The board setter provides a partially completed board, which for a well-posed board has a unique solution. As explained above, for this problem, it suffices to calculate whether a given sudoku board has a solution. No need to return the actual numbers that make up a solution.

A sudoku board is represented as a two-dimensional 9x9 array of the characters ‘1’,‘2’,…,‘9’ and the "." character, which represents a blank space. The function should fill the blank spaces with characters such that the following rules apply:
In every row of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
In every column of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
In every 3x3 sub-board that is illustrated below, all characters ‘1’,‘2’,…,‘9’ appear exactly once.

A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with characters that abide to the constraints above. If the function succeeds in solving the sudoku board, it’ll return true (false, otherwise).

Resources:

runtime: 

"""

# Solution techniques are Backtracking

# Time complexity : O(n * m) ? Space complexity : O()
# O(n ^ m) where n is the number of possibilities for each square (i.e., 9 in classic Sudoku) and m is the number of spaces that are blank.

""" 
The most straightforward way to build a sudoku solver is a recursive backtracking algorithm. In such an algorithm, we change one cell of the board (possibly multiple times) and call our function again to ask whether that board can be solved.

What the program should do at a high level is this: choose an empty cell and place values inside. If some placed value makes solve(board) true, then the answer is true - otherwise, the answer is false.

If your peer has not considered it or is choosing the “empty cell” naively, ask them what choice of empty cell would be best. If still stuck, clarify that we want to choose an empty cell that will have us do the least work later.

The best choice of an empty cell is the choice with the least possibilities, because in the worst case we will check sudokuSolve(board) the least times. Encourage your peer to write a helper function getCandidates that gets the possibilities of what values some cell board[r][c] could be.
"""


def getCandidates(board, row, col):
    candidates = []
    block_i = (row - row % 3)
    block_j = (col - col % 3)

    # for each candidate value in range 1-10 check if it is unique in given cells entire row, col and block. If no collision append it to candidates list
    for no in range(1, 10):
        num = str(no)
        collision = False

        for i in range(9):
            if (board[row][i] == num or
                board[i][col] == num or
                    board[block_i + (i // 3)][block_j + (i % 3)] == num):
                collision = True
                break

        if (not collision):
            candidates.append(num)

    return candidates


def sudoku_solve(board):
    row = -1
    col = -1
    candidates = None

    # the purpose of this section is to find the row and col of the cell with the smallest, possible candidate list
    for r in range(9):
        for c in range(9):
            if (board[r][c] == "."):
                newCandidates = getCandidates(board, r, c)

                if (candidates is None or len(newCandidates) < len(candidates)):
                    candidates = newCandidates
                    row = r
                    col = c

    # if there is no empty cell (no candidates needed for any cell in the entire matrix) return True as board is solved
    if (candidates is None):
        return True

    # This part is backtracking, we put one of the candidate values in sudoku matrix location and recursively call this fuction to check if the entier board is solved. This function (sudoku_solve) will return true if candidates is None which would happen if no empty cell remaining in board
    # Otherwise it will return false if all candidates exhausted and board not solved
    # If false we erase the cell by turning it back into a "." cell and move on to the next candidate until all candidates are exhausted [AKA Backtrack]
    for val in candidates:
        board[row][col] = val

        if (sudoku_solve(board)):
            return True

        board[row][col] = "."

    return False


# inpt = [[".", "8", "9", ".", "4", ".", "6", ".", "5"],
#         [".", "7", ".", ".", ".", "8", ".", "4", "1"],
#         ["5", "6", ".", "9", ".", ".", ".", ".", "8"],
#         [".", ".", ".", "7", ".", "5", ".", "9", "."],
#         [".", "9", ".", "4", ".", "1", ".", "5", "."],
#         [".", "3", ".", "9", ".", "6", ".", "1", "."],
#         ["8", ".", ".", ".", ".", ".", ".", ".", "7"],
#         [".", "2", ".", "8", ".", ".", ".", "6", "."],
#         [".", ".", "6", ".", "7", ".", ".", "8", "."]]

# output - False

inpt = [
    [".", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["1", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]]

# output - False

print(sudoku_solve(inpt))
