#!/bin/python3
""" Disjoint Set Union Find """

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the maxCircle function below.


class Disjoint_Set():
    def __init__(self, nodes):
        # Key - node , Value - size of the set/tree/component rooted at given node
        self.size = defaultdict(int)
        # Key - node , Value - Parent/Root node
        self.roots = defaultdict(int)
        self.initialize(nodes)
        self.largestSet = 0

    def initialize(self, nodes):
        for n in nodes:
            self.roots[n] = n
            self.size[n] = 1

    # Optimized using Union by Size / Rank (Merge smaller trees to larger trees, to maintain balance and keep trees flat)
    def union(self, node_A, node_B):
        root_A = self.findRoot(node_A)
        root_B = self.findRoot(node_B)

        if root_A != root_B:
            if self.size[root_A] < self.size[root_B]:
                self.roots[root_A] = root_B
                self.size[root_B] += self.size[root_A]
                self.largestSet = max(self.largestSet, self.size[root_B])
            else:
                self.roots[root_B] = root_A
                self.size[root_A] += self.size[root_B]
                self.largestSet = max(self.largestSet, self.size[root_A])

    # Optimized using Path Compression (Make every other node in path point to it's grandparent, keeps trees flat)
    def findRoot(self, node):
        if self.roots[node] == node:
            return node

        self.roots[node] = self.findRoot(self.roots[node])

        return self.roots[node]

    def find(self, node_A, node_B):
        return self.findRoot(node_A) == self.findRoot(node_B)

    def largest_friend_circle(self):
        return self.largestSet


def maxCircle(queries):
    ans = []

    unique_nodes = set()

    for a, b in queries:
        unique_nodes.add(a)
        unique_nodes.add(b)

    ds = Disjoint_Set(unique_nodes)

    # print(ds.parents)
    # print(ds.size)

    for nodeA, nodeB in queries:
        ds.union(nodeA, nodeB)
        largest = ds.largest_friend_circle()
        ans.append(largest)

    return ans


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)
    print(ans)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
