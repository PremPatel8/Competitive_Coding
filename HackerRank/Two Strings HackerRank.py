#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_dict = {}
    s2_dict = {}

    for x in s1:
        if x in s1_dict:
            s1_dict[x] += 1
        else:
            s1_dict[x] = 1

    for x in s2:
        if x in s2_dict:
            s2_dict[x] += 1
        else:
            s2_dict[x] = 1

    if len(s1)<len(s2):
        for x in s1_dict:
             if x in s2_dict:
                return "YES"
    else:
        for x in s2_dict:
            if x in s1_dict:
                return "YES"

    return "NO"
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
