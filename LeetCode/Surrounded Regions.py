from typing import Deque, List
from itertools import product
from collections import deque

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
https://leetcode.com/problems/surrounded-regions/discuss/691646/Python-O(mn)-3-colors-dfs-explained
https://leetcode.com/problems/surrounded-regions/discuss/41652/Python-easy-to-understand-DFS-and-BFS-solutions
https://leetcode.com/problems/surrounded-regions/discuss/41630/9-lines-Python-148-ms

https://leetcode.com/problems/surrounded-regions/discuss/171506/It's-important-to-master-all-3-methods%3A-DFS-BFS-Union-Find


runtime: 
59 / 59 test cases passed.
	Status: Accepted
Runtime: 144 ms
Memory Usage: 15.8 MB
"""

# Solution techniques are Union Find solution

# Time complexity : O(), Space complexity : O()


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        parents = {}

        for r in range(len(board)):
            for c in range(len(board[r])):
                if r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1:
                    self.traverse(board, parents, r, c, -1, -1)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'O' and parents.get((r, c)) != (-1, -1):
                    board[r][c] = 'X'

        # print(board)

    def traverse(self, board, parents, r, c, pr, pc):
        if (r, c) in parents or r < 0 or r > len(board)-1 or c < 0 or c > len(board[0])-1 or board[r][c] != 'O':
            return
        else:
            parentCurr = self.find((r, c), parents)
            parentPrev = self.find((pr, pc), parents)
            if parentCurr != parentPrev:
                parents[parentCurr] = parentPrev
            self.traverse(board, parents, r+1, c, r, c)
            self.traverse(board, parents, r-1, c, r, c)
            self.traverse(board, parents, r, c+1, r, c)
            self.traverse(board, parents, r, c-1, r, c)

    def find(self, node, parents):
        if node not in parents:
            parents[node] = node
            return node
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]


myobj = Solution()
inpt = [['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']]
myobj.solve(inpt)
