""" shortest path
https://structy.net/problems/shortest-path

Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.
test_00:

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'w', 'z') # -> 2
"""

from collections import deque


def shortest_path(edges, node_A, node_B):
    graph = constructGraph(edges)
    shortest_path_len = float("inf")

    res = bfs_iterative(graph, node_A, node_B)

    shortest_path_len = min(shortest_path_len, res)

    return shortest_path_len


def bfs_iterative(graph, node_A, node_B):
    shortest_path = float("inf")
    queue = deque()
    queue.append((node_A, 0))
    visited = set()

    while queue:
        curr = queue.popleft()

        if curr[0] == node_B:
            return curr[1]

        if curr not in visited:
            visited.add(curr[0])

            for neighbour in graph[curr[0]]:
                if neighbour not in visited:
                    queue.append((neighbour, curr[1]+1))

    return -1


def constructGraph(edges):
    graph = {}

    for v1, v2 in edges:
        graph[v1] = graph.get(v1, [])+[v2]
        graph[v2] = graph.get(v2, [])+[v1]

    return graph
