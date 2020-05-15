#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(Q):

    moves = 0 

    Q = [P-1 for P in Q]

    # print(q)
    print(Q)

    for i,P in enumerate(Q):
        print(f"i={i}")
        print(f"p={P}")

        if P - i > 2:
            print("Too chaotic")
            return

        print("range =",*range(max(P-1,0),i))

        for j in range(max(P-1,0),i):
            print(f"Q[{j}] = {Q[j]} , P={P}")
            if Q[j] > P:
                print("move increment")
                moves += 1
    print(moves)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        # q = [1, 2, 5, 3, 7, 8, 6, 4]

        minimumBribes(q)
