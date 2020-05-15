#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the triplets function below.
def triplets(a, b, c):
    result = 0 
    abDict = defaultdict(set)

    for x in a:
        for y in b:
            if x <= y:
                abDict[x].add(y)
    
    # print(f"abDict = {abDict}")

    for x in abDict:
        for y in abDict[x]:
            for z in c:
                # print(f"x, y, z = {x,y,z}")
                if y >= z:
                    # print(f"Inside x, y, z = {x,y,z}")
                    result += 1
    
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    print(f"ans = {ans}")

    # fptr.write(str(ans) + '\n')

    # fptr.close()
