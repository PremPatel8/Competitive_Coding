""" connected components count
https://structy.net/problems/connected-components-count

Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.
test_00:

connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2
"""

from collections import deque


def connected_components_count(graph):
    componentCount = 0
    visited = set()

    for node in graph:
        if node not in visited:
            # dfs_iterative(graph, node, visited)
            bfs_iterative(graph, node, visited)
            componentCount += 1

    return componentCount

# def dfs_recursive(graph, node, visited):
#   if node in visited:
#     return False

#   visited.add(node)

#   for neighbour in graph[node]:
#     dfs_recursive(graph, neighbour, visited)

#   return True

# def dfs_iterative(graph, node, visited):
#     stack = deque()
#     stack.append(node)

#     while(stack):
#         curr = stack.pop()

#         if curr not in visited:
#             visited.add(curr)

#             for neighbour in graph[curr]:
#                 if neighbour not in visited:
#                     stack.append(neighbour)

#     return True


def bfs_iterative(graph, node, visited):
    queue = deque()
    queue.append(node)

    while(queue):
        curr = queue.popleft()

        if curr not in visited:
            visited.add(curr)

            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append(neighbour)
