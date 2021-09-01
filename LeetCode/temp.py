# from collections import deque


# def connected_components_count(graph):
#     componentCount = 0
#     visited = set()

#     for node in graph:
#         if node not in visited:
#             dfs_recursive(graph, node, visited)
#             # dfs_iterative(graph, node, visited)
#             # bfs_iterative(graph, node, visited)
#             componentCount += 1

#     return componentCount


# def dfs_recursive(graph, node, visited):
#     if node in visited:
#         return

#     visited.add(node)

#     for neighbour in graph[node]:
#         if neighbour not in visited:
#             dfs_recursive(graph, neighbour, visited)

#     return


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


# def bfs_iterative(graph, node, visited):
#     queue = deque()
#     queue.append(node)

#     while(queue):
#         curr = queue.popleft()

#         if curr not in visited:
#             visited.add(curr)

#             for neighbour in graph[curr]:
#                 if neighbour not in visited:
#                     queue.append(neighbour)


# inpt = {
#     0: [8, 1, 5],
#     1: [0],
#     5: [0, 8],
#     8: [0, 5],
#     2: [3, 4],
#     3: [2, 4],
#     4: [3, 2]
# }  # -> 2

# print(connected_components_count(inpt))


inpt = "aaa bbb ccc bbb ddd aaa bbb ppp"

def top_n_most_frequent_word(inpt, count):
    


