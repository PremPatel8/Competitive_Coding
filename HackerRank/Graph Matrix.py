#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the minTime function below.


class Disjoint_Set():

    def __init__(self):
        self.parent = defaultdict(int)

    def make_set(self, city, is_machine):
        self.parent[city] = is_machine

    def Find(self, city):
        if self.parent[city] == city:
            return city
        else:
            return self.Find(self.parent[city])

    def Union(self, set1, set2):
        self.parent[set2] = self.parent[set1]

    def has_machine(self, city):
        return self.parent[city]


def minTime(roads, machines):
    minTime = 0
    roads.sort(key=lambda x: x[2], reverse=True)

    city_sets = Disjoint_Set()

    # print(roads)
    # print(sorted(machines))

    for m in machines:
        city_sets.make_set(m, True)

    # print(city_sets.parent)

    for c1, c2, time in roads:
        if city_sets.has_machine(c1) and city_sets.has_machine(c2):
            minTime += time
        else:
            city_sets.Union(c1, c2)

    return minTime


if __name__ == '__main__':
    fptr = open('D:/GitHub/Cometitive_Coding/HackerRank/Graph_Matrix.txt', 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()
