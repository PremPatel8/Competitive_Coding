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
https://leetcode.com/problems/course-schedule/discuss/441722/Python-99-time-and-100-space.-Collection-of-solutions-with-explanation

runtime: 
46 / 46 test cases passed.
	Status: Accepted
Runtime: 580 ms
Memory Usage: 15.1 MB
"""

# Solution techniques are DFS Solution

# Time complexity : O(V+E) Space complexity : O(V+E)


# https://leetcode.com/problems/course-schedule/discuss/441722/Python-99-time-and-100-space.-Collection-of-solutions-with-explanation

# DFS with vertex state array
# DFS with stack + set (Topological Sort)
# BFS kahn's algorithm with inDegree array and queue


class Solution:

    # Solution 1: DFS with an array storing 3 different states of a vertex

    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList

    """ 46 / 46 test cases passed.
            Status: Accepted
        Runtime: 88 ms
        Memory Usage: 16.7 MB """

    """ def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build Adjacency list from Edges list
        adjList = self.buildAdjacencyList(numCourses, prerequisites)

        # Each vertex can have 3 different states:
        # state 0   : vertex is not visited. It's a default state.
        # state -1  : vertex is being processed. Either all of its descendants
        #             are not processed or it's still in the function call stack.
        # state 1   : vertex and all its descendants are processed.
        state = [0] * numCourses

        def hasCycle(v):
            if state[v] == 1:
                # This vertex is processed so we pass.
                return False
            if state[v] == -1:
                # This vertex is being processed and it means we have a cycle.
                return True

            # Set state to -1
            state[v] = -1

            for i in adjList[v]:
                if hasCycle(i):
                    return True

            state[v] = 1
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v):
                return False

        return True """

# Solution 2: DFS with a stack storing all decendants being processed
# Same idea as Solution 1, this time we use a stack to store all vertices being processed. 
# While visiting a descendant of a vertex, if we found it in the stack it means a cycle appears.
# This technique is also used to find a Topological order from the graph.

    """ 46 / 46 test cases passed.
        Status: Accepted
    Runtime: 100 ms
    Memory Usage: 17.3 MB """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build Adjacency list from Edges list
        adjList = self.buildAdjacencyList(numCourses, prerequisites)
        visited = set()

        def hasCycle(v, stack):
            if v in visited:
                if v in stack:
                    # This vertex is being processed and it means we have a cycle.
                    return True
                # This vertex is processed so we pass
                return False

            # mark this vertex as visited
            visited.add(v)
            # add it to the current stack
            stack.append(v)

            for i in adjList[v]:
                if hasCycle(i, stack):
                    return True

            # once processed, we pop it out of the stack
            stack.pop()
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v, []):
                return False

        return True


# Solution 3: BFS with Kahn's algorithm for Topological Sorting
# This solution is usually seen in problems where we need to answer two questions:
# Is it possible to have a topological order?
# if yes then print out one of all the orders.

    """ 46 / 46 test cases passed.
	Status: Accepted
Runtime: 88 ms
Memory Usage: 15.3 MB """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        inDegrees = [0] * numCourses

        for c1, c2 in prerequisites:
            adjList[c2].append(c1)
            inDegrees[c1] += 1

        queue = deque(v for v in range(numCourses) if inDegrees[v] == 0)
        visited = 0

        while queue:
            v = queue.popleft()
            visited += 1

            # for each descendant of current vertex, reduce its in-degree by 1
            for des in adjList[v]:
                inDegrees[des] -= 1
                # if in-degree becomes 0, add it to queue
                if inDegrees[des] == 0:
                    queue.append(des)

        return visited == numCourses


myobj = Solution()
# numCourses = 2
# prerequisites = [[1, 0], [0, 1]]
# prerequisites = [[1, 0]]

numCourses = 8
prerequisites = [[0, 6], [1, 6], [1, 4], [1, 2],
                 [3, 0], [3, 4], [5, 1], [7, 0], [7, 1]]

# Expected Adjacency List: [0:[3, 7], 1:[5, 7], 2:[1], 3:[], 4:[1, 3], 5:[], 6:[0, 1], 7:[]]
#    0        1     2    3    4     5      6     7
# [[3, 7], [5, 7], [1], [], [1, 3], [], [0, 1], []]
# Explanation: Course 0 is a prerequisite for courses 3 & 7


print(myobj.canFinish(numCourses, prerequisites))
