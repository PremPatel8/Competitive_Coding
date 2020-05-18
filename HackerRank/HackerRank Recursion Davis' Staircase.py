#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.


def stepPerms(n):
    stArr = [0]*(n+1)

    def stepCalc(st):
        if st < 0:
            return 0
        elif st == 0:
            return 1
        if stArr[st] == 0:
            stArr[st] = stepCalc(st-1) + stepCalc(st-2) + stepCalc(st-3)
        
        return stArr[st]

    return stepCalc(n)


if __name__ == '__main__':
    res = stepPerms(5)

    print(f"res = {res}")
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = int(input())

    # for s_itr in range(s):
    #     n = int(input())

    #     res = stepPerms(n)

        # fptr.write(str(res) + '\n')

    # fptr.close()
