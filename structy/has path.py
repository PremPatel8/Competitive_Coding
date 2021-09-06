""" has path
https://structy.net/problems/has-path

Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
test_00:

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'k') # True
"""

from collections import deque


def has_path(graph, src, dst):
    """ DFS iterative solution """
    def dfs(graph, src, dst):
        stack = deque()
        stack.append(src)

        while stack:
            curr = stack.pop()

            if curr == dst:
                return True

            for neighbour in graph[curr]:
                stack.append(neighbour)

        return False

    """ DFS recursive solution """
    def dfs(graph, src, dst):
        if src == dst:
            return True

        for neighbour in graph[src]:
            res = dfs(graph, neighbour, dst)
            if res:
                return True

        return False

    """ BFS iterative solution """
    def bfs(graph, src, dst):
        queue = deque()
        queue.append(src)

        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True

            for neighbour in graph[curr]:
                queue.append(neighbour)

        return False

    res = bfs(graph, src, dst)
    # res = dfs(graph, src, dst)
    return res
