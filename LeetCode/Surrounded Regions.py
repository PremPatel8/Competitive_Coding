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
Runtime: 160 ms
Memory Usage: 16.5 MB
"""

# Solution techniques are
# first DFS all the border elements and mark all O's as T (these O's are not surrounded by X and will not be captured)
# Then iterate over each element in the matrix and convert all O's to X's and all T's back to O's

# Time complexity : O(m*n) where m and n are sizes of our board, Space complexity : O(mn) if you count the call stack


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or len(board) < 3 or len(board[0]) < 3:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != "O":
                return

            board[i][j] = 'T'
            neib_list = [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]

            for x, y in neib_list:
                dfs(x, y)

        # processing left and right border elements
        for i in range(0, rows):
            dfs(i, 0)
            dfs(i, cols-1)

        # processing top and bottom border elements
        for j in range(0, cols):
            dfs(0, j)
            dfs(rows-1, j)

        # product used to find the cartesian product
        for i, j in product(range(rows), range(cols)):
            board[i][j] = "X" if board[i][j] != "T" else "O"

        print(board)


myobj = Solution()
inpt = [['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']]
myobj.solve(inpt)
