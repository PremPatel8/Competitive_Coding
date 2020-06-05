#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the minTime function below.

class Disjoint_Set():
    parent = defaultdict()

def minTime(roads, machines):
    roads.sort(key=lambda x: x[2], reverse=True)


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
