#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    largest = 0
    temp = 0
    zero_arr = [0]*n

    for optn in queries:

        start_idx = optn[0]-1
        end_idx = optn[1]-1
        summand = optn[2]

        # print(f"start_idx, end_idx, summand = {start_idx, end_idx, summand}")

        zero_arr[start_idx] += summand

        if end_idx+1 <= n-1:
            zero_arr[end_idx+1] -= summand

    # print(zero_arr)

    for x in zero_arr:
        temp += x
        if largest<temp:
            largest = temp

    return largest


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(f"result = {result}")

    # fptr.write(str(result) + '\n')

    # fptr.close()
