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
Runtime: 212 ms
Memory Usage: 14.8 MB
"""

# Solution techniques are Disjoint Set, Union Find

# Time complexity : O((M+N) lg*N) for Weigted Union + Path Compression solution, Space complexity : O(n)
# Starting from an empty data structure, any sequenceof M union and find operations on N objects takes O(N + M lg* N) time.
# lg*N - number of times needed to take the lg of a number until reaching 1
# In practice time complexity is almost linear


class Disjoint_Set():
    def __init__(self, nodes):
        self.size = defaultdict(int)
        self.parents = defaultdict(int)
        self.initialize(nodes)
        self.largestSet = 0

    def initialize(self, nodes):
        for n in nodes:
            self.parents[n] = n
            self.size[n] = 1

    # Optimized using Union by Size / Rank
    def union(self, node_A, node_B):
        root_A = self.find(node_A)
        root_B = self.find(node_B)

        if root_A != root_B:
            if self.size[root_A] < self.size[root_B]:
                self.parents[root_A] = root_B
                self.size[root_B] += self.size[root_A]
                self.largestSet = max(self.largestSet, self.size[root_B])
            else:
                self.parents[root_B] = root_A
                self.size[root_A] += self.size[root_B]
                self.largestSet = max(self.largestSet, self.size[root_A])

    # Optimized using Path Compression
    def find(self, node):
        if self.parents[node] == node:
            return node

        self.parents[node] = self.find(self.parents[node])

        return self.parents[node]


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        rows = len(M)
        cols = len(M[0])
        res = rows
        students = [studNum for studNum in range(rows)]
        ds = Disjoint_Set(students)

        for i in range(rows):
            for j in range(cols):
                if i != j and M[i][j] == 1:
                    parent_a = ds.find(i)
                    parent_b = ds.find(j)

                    if parent_a != parent_b:
                        ds.union(i, j)
                        res -= 1
        return res


myobj = Solution()
inpt = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]]
print(myobj.findCircleNum(inpt))
