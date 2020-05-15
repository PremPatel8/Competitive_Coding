#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    cnt = 0
    # print(q)

    for idx, val in enumerate(q):
        # print(f"idx = {idx}")
        # print(f"val = {val}")

        res = (val-1)-idx
        # print("res = ",res)

        if res > 2:
            print("Too chaotic")
            return

        # print("range =",*range(max(val-2, 0), idx))

        for j in range(max(val-2, 0), idx):
            # print(f"q[{j}] = {q[j]} , val={val}")
            if q[j] > val:
                # print("move increment")
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
