from typing import List

"""
Problem Name: Valid Sudoku

Problem Section: Array

Problem Statement:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

Resources:
"""
""" 504 / 504 test cases passed.
	Status: Accepted
Runtime: 92 ms
Memory Usage: 14 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() straightforward solution


class Solution:
    def isValidSudoku(self, board):
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y]
                          for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)


# My solution with alt is_unit_valid() function
    """
507 / 507 test cases passed.
	Status: Accepted
Runtime: 96 ms
Memory Usage: 14.4 MB
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rowCheck = self.checkRow(board)
        colCheck = self.checkCol(board)
        boxCheck = self.checkBox(board, rows, cols)

        # print(f"rowCheck = {rowCheck}, colCheck = {colCheck}, boxCheck = {boxCheck}")

        return rowCheck and colCheck and boxCheck

    def checkRow(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False

        return True

    def checkCol(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False

        return True

    def checkBox(self, board, rows, cols):
        # print(f"rows={rows}, cols = {cols}")

        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                # print(f"i={i}, j={j}")

                seen = set()
                for r in range(rows//3):
                    for c in range(cols//3):
                        ele = board[i+r][j+c]

                        if ele != '.':
                            if ele in seen:
                                return False
                            else:
                                seen.add(ele)
        return True

    def is_unit_valid(self, unit):
        seen = set()

        for ele in unit:
            if ele != '.':
                if ele in seen:
                    return False
                else:
                    seen.add(ele)

        return True


myobj = Solution()
# inpt = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
# inpt = [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]

inpt = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]
print(myobj.isValidSudoku(inpt))
