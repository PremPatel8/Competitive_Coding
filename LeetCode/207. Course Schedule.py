from typing import List
from collections import defaultdict

"""
Problem Name: 207. Course Schedule

Problem URL: https://leetcode.com/problems/course-schedule/

Problem Section: 

Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Constraints:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5


Resources:
https://youtu.be/2l22FRtU45M?list=TLPQMDkxMTIwMjAsLK6Zf6XLXg&t=847

runtime: 
46 / 46 test cases passed.
	Status: Accepted
Runtime: 580 ms
Memory Usage: 15.1 MB
"""

# Solution techniques are Kahn's algorithm

# Time complexity : O(N+E) Space complexity : O(N)?


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0]*numCourses
        zeroDegree = set()

        for i, j in prerequisites:
            inDegree[i] += 1

        for i in range(numCourses):
            if inDegree[i] == 0:
                zeroDegree.add(i)

        if len(zeroDegree) == 0:
            return False

        while zeroDegree:
            course = zeroDegree.pop()

            for i, j in prerequisites:
                if course == j:
                    inDegree[i] -= 1

                    if inDegree[i] == 0:
                        zeroDegree.add(i)

        for num in inDegree:
            if num != 0:
                return False

        return True


myobj = Solution()
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
# prerequisites = [[1, 0]]

print(myobj.canFinish(numCourses, prerequisites))
