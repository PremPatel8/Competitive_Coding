#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    
    visited = [0] * len(arr)

    list_pairs = []

    ans = 0

    for idx, x in enumerate(arr):
        # print(f"x = {x}, idx = {idx}")

        list_pairs.append([x,idx])

    # print(list_pairs)

    list_pairs.sort(key=lambda x: x[0])

    # print(list_pairs)

    for idx, x in enumerate(arr):
        # print(f"list_pairs[{idx}][1] = {list_pairs[idx][1]}")

        if visited[idx] or list_pairs[idx][1] == idx:
            continue;
        
        cycle_size = 0

        j = idx

        while not(visited[j]):
            visited[j] = 1
            j = list_pairs[j][1]
            cycle_size += 1

        ans += cycle_size-1


    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
