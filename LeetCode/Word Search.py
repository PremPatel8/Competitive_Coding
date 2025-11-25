from typing import List
from collections import Counter
from itertools import chain

"""
Problem Name: Word Search

Problem Section: Backtracking

Problem Statement:
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:
board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

""" 89 / 89 test cases passed.
	Status: Accepted
Runtime: 200 ms
Memory Usage: 15.7 MB """

# Backtrackin with some optimization
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, idx):
            # First: validate current cell index boundaries and value
            if not (0 <= row < rows) or not (0 <= col < cols) or board[row][col] != word[idx]:
                return False
            # Then: if last character matched, success!
            if idx == len(word) - 1:
                return True

            # Mark as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Explore neighbors
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                if backtrack(row + dr, col + dc, idx + 1):
                    board[row][col] = temp  # restore before returning
                    return True

            board[row][col] = temp
            return False

        
        rows, cols = len(board), len(board[0])
        
        # Early Termination & Pruning (Optimization)
        if not ((rows * cols) >= len(word)):
            return False
        
        # If the board doesn’t contain enough of each character in word, return False early.
        if Counter(word) - Counter(ch for row in board for ch in row):
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False


myobj = Solution()

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCCED"
# word = "PREM"
print(myobj.exist(board, word))
