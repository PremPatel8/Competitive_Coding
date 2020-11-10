from typing import List
from collections import deque


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

# Solution techniques are Optimized BFS Kahn's algorithm

# Time complexity : O(V+E) Space complexity : O(V+E)


class Solution:
    # Algorithm: BFS Topological Sorting
    # Time: O(E + V)
    # Space: O(E + V)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0, ] * numCourses

        for to_, from_ in prerequisites:
            graph[from_].append(to_)
            indegree[to_] += 1

        queue = deque(v for v in range(numCourses) if indegree[v] == 0)
        n = len(queue)

        while queue and n != numCourses:
            v = queue.popleft()
            for to_ in graph[v]:
                indegree[to_] -= 1
                if indegree[to_] == 0:
                    n += 1
                    queue.append(to_)

        return n == numCourses


myobj = Solution()
numCourses = 2
# prerequisites = [[1, 0], [0, 1]]
prerequisites = [[1, 0]]

print(myobj.canFinish(numCourses, prerequisites))
