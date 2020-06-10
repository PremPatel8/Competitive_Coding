#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.


class BinTrie:
    head = {}

    def add(self, integer):
        cur = self.head
        b = "{:032b}".format(integer)

        for l in b:
            l = int(l)
            if l not in cur:
                cur[l] = {}
            cur = cur[l]
        cur['*'] = True

    def max_companion(self, integer):
        cur = self.head
        b = "{:032b}".format(integer)
        m_comp = ''

        for l in b:
            l = int(l)
            opp = l ^ 1
            if opp in cur:
                l = opp
            cur = cur[l]
            m_comp += str(l)    
        return int(m_comp, 2)


def maxXor(arr, queries):
    d = BinTrie()

    out = []

    for x in arr:
        d.add(x)

    print(d.head)

    for v in queries:
        out.append(v ^ d.max_companion(v))

    return out


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
