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
Runtime: 384 ms
Memory Usage: 15.4 MB """


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenX, lenY = len(board), len(board[0])
        lenW = len(word)

        def dfs(x, y, idx):
            if idx == lenW:
                return True
            if (x < 0 or x >= lenX) or (y < 0 or y >= lenY) or board[x][y] != word[idx]:
                return False

            tmp = board[x][y]
            board[x][y] = "#"
            idx += 1

            if dfs(x-1, y, idx) or dfs(x, y-1, idx) or dfs(x+1, y, idx) or dfs(x, y+1, idx):
                # board[x][y] = tmp
                return True
            else:
                board[x][y] = tmp
                return False

        for i in range(lenX):
            for j in range(lenY):
                if dfs(i, j, 0):
                    return True

        return False


myobj = Solution()

bord = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

# word = "ABCCED"
word = "PREM"
print(myobj.exist(bord, word))
