from typing import List

"""
Problem Name: 51. N-Queens

Problem URL: https://leetcode.com/problems/n-queens/description/

Problem Section: Backtracking

Problem Difficulty: Medium / Hard

Problem Statement:
[51. N-Queens](https://leetcode.com/problems/n-queens/) The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.
 
Given an integer `n`, return  *all distinct solutions to the **n-queens puzzle*** . You may return the answer in **any order**.
 
Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.
 
**Example 1:**
![Image](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
 
**Input:** n = 4
**Output:** `[".Q..", "...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]`
**Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above
 
**Example 2:**
**Input:** n = 1
**Output:** [["Q"]]
 
**Constraints:**
 
- `1 <= n <= 9`

Resources:

"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, diagonals, anti_diagonals, cols, board_state):
            # Base case - N queens have been placed
            if row == n:
                result.append(create_board(board_state))
                return

            for col in range(n):
                # For each square on a given diagonal, the difference between the row and column indices (row - col) will be constant. 
                curr_diagonal = row - col
                
                # For each square on a given anti-diagonal, the sum of the row and column indexes (row + col) will be constant
                curr_anti_diagonal = row + col
                
                # If the queen is not placeable
                if (
                    col in cols
                    or curr_diagonal in diagonals
                    or curr_anti_diagonal in anti_diagonals
                ):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                board_state[row][col] = "Q"

                # Move on to the next row with the updated board state
                backtrack(row + 1, diagonals, anti_diagonals, cols, board_state)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                board_state[row][col] = "."

        result = []
        board_state = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board_state)
        return result


response = Solution().solveNQueens(4)
print(response)
print(response == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
