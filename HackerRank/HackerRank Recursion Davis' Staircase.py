#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.


def stepPerms(n):
    st = 0
    stArr = {}

    def stepCalc(st):
        if st in stArr:
            return stArr[st]
        elif st > n:
            return 0
        elif st == n:
            return 1
        else:
            val = stepCalc(st+1) + stepCalc(st+2) + stepCalc(st+3)
            stArr[st] = val
            return val

    return stepCalc(st)


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
