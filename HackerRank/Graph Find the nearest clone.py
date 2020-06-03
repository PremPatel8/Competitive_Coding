#!/bin/python3

import math
import os
import random
import re
import sys
import pprint
from collections import defaultdict, Counter

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    colorFreq = Counter(ids)

    if colorFreq[val] <= 1:
        return -1

    nodeList = []
    shortestPathLen = 1000000000

    for f, t in zip(graph_from, graph_to):
        nodeList.append([f, t])

    colorGraph = Graph(nodeList)

    # pretty_print = pprint.PrettyPrinter()
    # pretty_print.pprint(colorGraph._graph)

    nodesOfReqiredColor = []

    for i, id in enumerate(ids):
        if id == val:
            nodesOfReqiredColor.append(i+1)

    # print(nodesOfReqiredColor)

    for i, startNode in enumerate(nodesOfReqiredColor):
        for endNode in nodesOfReqiredColor[i+1:]:
            pathLen = bfs_paths(colorGraph._graph, startNode, endNode)

            shortestPathLen = min(shortestPathLen, pathLen)

    return shortestPathLen


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex]-set(path):
            if next == goal:
                return len(path + [next])-1
            else:
                queue.append((next, path + [next]))


if __name__ == '__main__':
    fptr = open(
        'D:/GitHub/Cometitive_Coding/HackerRank/Find_Nearest_Clone.txt', 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
