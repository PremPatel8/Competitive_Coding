from typing import List
from itertools import product

"""
Problem Name: Surrounded Regions

Problem URL: https://leetcode.com/problems/surrounded-regions/

Problem Section: DFS, BFS, Union Find

Problem Statement:
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


Resources:

runtime: 
59 / 59 test cases passed.
	Status: Accepted
Runtime: 188 ms
Memory Usage: 15.5 MB
"""

# Solution techniques are Optimized DFS solution
# first add all border elements row, col as tuples to a stack
# Then pop row, col tuples from the stack till stack is not empty, for each row, col, if it's a valid coordinate and the value at the coordinate is "O"
# Change the "O" to "T" as this "O" is not surrounded and cannot be captured
# append the top, bottom, left and right coordinates for the current coordinate to the stack and repeate from step 1 till stack is exhausted (Iterative DFS)
# Then iterate over each element in the matrix and convert all O's to X's and all T's back to O's

# Time complexity : O(m*n) where m and n are sizes of our board, Space complexity : O(mn) for the stack


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or len(board) < 3 or len(board[0]) < 3:
            return

        rows = len(board)
        cols = len(board[0])
        stack = []

        # Adding border elements to stack
        for k in range(max(rows, cols)):
            for i, j in ((k, 0), (k, cols-1), (0, k), (rows-1, k)):
                stack.append((i, j))

        while stack:
            i, j = stack.pop()

            if 0 <= i < rows and 0 <= j < cols and board[i][j] == "O":
                board[i][j] = "T"
                stack.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

        # board[:] = [['X' if c != 'T' else 'O' for c in row] for row in board]
        for row in range(rows):
            for col in range(cols):
                board[row][col] = "X" if board[row][col] != "T" else "O"

        print(board)


myobj = Solution()
inpt = [['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']]
myobj.solve(inpt)
