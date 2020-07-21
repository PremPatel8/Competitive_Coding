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

# Using counter to check if the board has the necessary char frequency (no. of each char) to contain the target word before iterating through the board
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        board_counter, word_counter = Counter(chain(*board)), Counter(word)
        if word_counter - board_counter:
            return False

        rows, cols, chars = len(board), len(board[0]), len(word)
        gradients = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i: int, j: int, idx: int = 0):
            if not (0 <= i < rows and 0 <= j < cols) or board[i][j] != word[idx]:
                return False

            if idx == chars - 1:
                return True

            cell_value, board[i][j] = board[i][j], '#'

            if any(dfs(i + di, j + dj, idx + 1) for (di, dj) in gradients):
                return True

            board[i][j] = cell_value

            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c):
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
