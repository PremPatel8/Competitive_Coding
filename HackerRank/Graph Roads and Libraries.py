#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.

from collections import defaultdict
count = 0


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

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def DFS(visited, graph, node):
    if node not in visited:
        visited.add(node)
        global count
        count += 1
        for neighbour in list(graph[node]):
            DFS(visited, graph, neighbour)


def roadsAndLibraries(n, c_lib, c_road, cities):
    # If cost of building roads is equal to or greater than the cost of building libraries,
    # Just build a library in each city/node
    if c_road >= c_lib:
        return n * c_lib

    # Generating a Dictionary of sets as a graph data structure representation. Adjacency List? 
    mapGraph = Graph(cities)

    visited = set()
    componentNodes = []
    cost = 0

    for i in range(1, n+1):
        if i not in mapGraph._graph:
            mapGraph.add(i, i)

    for v in mapGraph._graph:
        if v not in visited:
            DFS(visited, mapGraph._graph, v)
            global count
            componentNodes.append(count)
            count = 0

    for nodes in componentNodes:
        cost += (nodes-1)*c_road+c_lib

    return cost


if __name__ == '__main__':
    fptr = open(
        'D:/GitHub/Cometitive_Coding/HackerRank/Roads_&_Libraries.txt', 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
