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

# Backtracking with some optimization
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        
        # Early Termination & Pruning (Optimization)
        if not ((rows * cols) >= len(word)):
            return False
        
        # If the board doesn’t contain enough of each character in word, return False early.
        if Counter(word) - Counter(ch for row in board for ch in row):
            return False
        
        def backtrack(row, col, word_idx):
            # First: validate current cell index boundaries and value
            if not (0 <= row < rows) or not (0 <= col < cols) or board[row][col] != word[word_idx]:
                return False
            
            # Then: if last character matched, success!
            if word_idx == len(word) - 1:
                return True

            # Mark as visited temporarily, so that it does not get reused when exploring neighboring cells
            temp = board[row][col]
            board[row][col] = '#'

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                if backtrack(nr, nc, word_idx+1):
                    board[row][col] = temp  # restore before returning
                    return True

            board[row][col] = temp
            return False

        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False
    
    
"""
Variation : Revisiting the same letter cell is allowed

If the constraint is changed to allow revisiting the same letter cell, the problem transitions from finding a path (no repeating nodes) to finding a walk (repeating nodes allowed).

Without the "no-reuse" constraint, the problem structure changes significantly. In the original version, the "visited" state makes the search path-dependent. If reuse is allowed, the answer for backtrack(row, col, word_idx) depends only on the current coordinates and the current index of the word.

Heuristic Hint: Since multiple paths could lead to the same cell at the same word_idx, you would likely encounter many redundant calculations.
Optimization: You could use Memoization (e.g., @cache in Python) to store the result of (row, col, word_idx). This would turn the time complexity into O(Rows×Cols×WordLength).
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # Dictionary to store results of (row, col, word_idx)
        memo = {}

        def backtrack(row, col, word_idx):
            # Check memo first
            if (row, col, word_idx) in memo:
                return memo[(row, col, word_idx)]
            
            # Validate current cell index boundaries and value
            if not (0 <= row < rows) or not (0 <= col < cols) or board[row][col] != word[word_idx]:
                return False
            
            # If last character matched, success!
            if word_idx == len(word) - 1:
                return True

            # Explore neighbors without marking the board
            for dr, dc in directions:
                if backtrack(row + dr, col + dc, word_idx + 1):
                    memo[(row, col, word_idx)] = True
                    return True

            # Store result in memo before returning
            memo[(row, col, word_idx)] = False
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
