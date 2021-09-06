""" largest component
https://structy.net/problems/largest-component

Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.
test_00:

largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4
"""

from collections import deque


def largest_component(graph):
    res = 0
    visited = set()

    for node in graph:
        if node not in visited:
            # count = dfs_iterative(graph, node, visited)
            # count = dfs_recursive(graph, node, visited)
            count = bfs_iterative(graph, node, visited)
            res = max(res, count)

    return res

# def dfs_iterative(graph, node, visited):
#   stack = deque()
#   stack.append(node)
#   size = 0

#   while stack:
#     currNode = stack.pop()

#     if currNode not in visited:
#       visited.add(currNode)
#       size += 1

#       for neighbour in graph[currNode]:
#         if neighbour not in visited:
#           stack.append(neighbour)

#   return size


# def dfs_recursive(graph, node, visited):
#   if node in visited:
#     return 0

#   visited.add(node)

#   count = 1

#   for neighbour in graph[node]:
#     count += dfs_recursive(graph, neighbour, visited)

#   return count


def bfs_iterative(graph, node, visited):
    stack = deque()
    stack.append(node)
    size = 0

    while stack:
        currNode = stack.popleft()

        if currNode not in visited:
            visited.add(currNode)
            size += 1

            for neighbour in graph[currNode]:
                if neighbour not in visited:
                    stack.append(neighbour)

    return size
