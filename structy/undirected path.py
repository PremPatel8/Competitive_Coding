""" undirected path
https://structy.net/problems/undirected-path

Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
test_00:

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True
"""

from collections import deque


def undirected_path(edges, node_A, node_B):
    graph = buildGraph(edges)
    # print(graph)
    # return dfs(graph, node_A, node_B)
    # return dfs(graph, node_A, node_B, set())
    return bfs(graph, node_A, node_B)


""" DFS iterative solution """


# def dfs(graph, src, dst):
#     stack = deque()
#     stack.append(src)
#     visited = set()

#     while stack:
#         curr = stack.pop()

#         if curr not in visited:
#             if curr == dst:
#                 return True

#             visited.add(curr)

#             for neighbour in graph[curr]:
#                 stack.append(neighbour)

#     return False

# def dfs(graph, src, dst, visited):
#     if src == dst:
#         return True

#     if src in visited:
#         return False

#     visited.add(src)

#     for neighbour in graph[src]:
#         if dfs(graph, neighbour, dst, visited) == True:
#             return True

#     return False

def bfs(graph, src, dst):
    queue = deque()
    queue.append(src)
    visited = set()

    while queue:
        curr = queue.popleft()

        if curr not in visited:
            if curr == dst:
                return True

            visited.add(curr)

            for neighbour in graph[curr]:
                queue.append(neighbour)

    return False


def buildGraph(edges):
    graph = {}

    for a, b in edges:
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]

    return graph
