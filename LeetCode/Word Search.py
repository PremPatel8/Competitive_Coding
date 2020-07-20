from typing import List

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
Runtime: 436 ms
Memory Usage: 15.6 MB """


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        def DFS(board, i, j, word):
            if len(word) == 0:
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False

            tmp = board[i][j]
            board[i][j] = "#"

            res = DFS(board, i+1, j, word[1:]) or DFS(board, i-1, j, word[1:]) \
                or DFS(board, i, j+1, word[1:]) or DFS(board, i, j-1, word[1:])

            board[i][j] = tmp
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if DFS(board, r, c, word):
                    return True

        return False


myobj = Solution()

bord = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCCED"
print(myobj.exist(bord, word))
