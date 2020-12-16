from typing import List
from collections import defaultdict

"""
Problem Name: Friend Circles

Problem URL: https://leetcode.com/problems/friend-circles/

Problem Section: Disjoint Set, Union Find, Graph

Problem Statement:
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]

Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

 
Constraints:
1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]


Resources:
https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
HackerRank Friend Circle Queries question
Evernote note

runtime: 
113 / 113 test cases passed.
	Status: Accepted
Runtime: 196 ms
Memory Usage: 14.8 MB
"""

# Solution techniques are Disjoint Set, Union Find

# Time complexity : O((M+N) lg*N) for Weigted Union + Path Compression solution, Space complexity : O(n)
# Starting from an empty data structure, any sequenceof M union and find operations on N objects takes O(N + M lg* N) time.
# lg*N - number of times needed to take the lg of a number until reaching 1
# In practice time complexity is almost linear


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # Optimized using Union by Size / Rank (Merge smaller trees to larger trees, to maintain balance and keep trees flat)
        def union(node_A, node_B):
            root_A = findRoot(node_A)
            root_B = findRoot(node_B)

            if size[root_A] < size[root_B]:
                root[root_A] = root_B
                size[root_B] += size[root_A]
            else:
                root[root_B] = root_A
                size[root_A] += size[root_B]

        # Optimized using Path Compression (Make every other node in path point to it's grandparent, keeps trees flat)
        def findRoot(node):
            if root[node] == node:
                return node

            root[node] = findRoot(root[node])

            return root[node]

        rows = len(M)
        cols = len(M[0])
        res = rows
        # Key - node , Value - size of the set/tree/component rooted at given node
        size = defaultdict(int)
        # Key - node , Value - Parent/Root node
        root = defaultdict(int)

        # Initializing root and size dicts with default values, each node is it's own root and each node has a size of 1 initially
        for studentNum in range(rows):
            root[studentNum] = studentNum
            size[studentNum] = 1

        for i in range(rows-1):
            for j in range(i+1, cols):
                if i != j and M[i][j] == 1 and findRoot(i) != findRoot(j):
                    union(i, j)
                    res -= 1

        return res


myobj = Solution()
inpt = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]]
print(myobj.findCircleNum(inpt))
