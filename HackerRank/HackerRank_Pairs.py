#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    # print(f"k = {k}")
    # print(f"arr = {arr}")
    
    nuSet = set()
    resultCount = 0

    for x in arr:
        nuSet.add(x)
    
    # print(f"nuSet = {nuSet}")
    
    for x in nuSet:
        if x+k in nuSet:
            resultCount += 1
    
    return resultCount

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(f"result = {result}")

    # fptr.write(str(result) + '\n')

    # fptr.close()
