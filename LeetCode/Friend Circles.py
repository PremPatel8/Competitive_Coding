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
Runtime: 224 ms
Memory Usage: 15 MB
"""

# Solution techniques are DFS

# Time complexity : O(), Space complexity : O()


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def check_friends_DFS(student: int) -> None:
            for friend, isFriend in enumerate(M[student]):
                if isFriend and friend not in seen:
                    seen.add(friend)
                    check_friends_DFS(friend)

        res = 0
        seen = set()

        for studentNum in range(len(M)):
            if studentNum not in seen:  # Found the start of a new circle.
                res += 1
                seen.add(studentNum)
                check_friends_DFS(studentNum)

        return res


myobj = Solution()
inpt = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]]
print(myobj.findCircleNum(inpt))
