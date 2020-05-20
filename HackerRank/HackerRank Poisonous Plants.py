#!/bin/python3

import math
import os
import random
import re
import sys


# This solution works but is too slow
# Complete the poisonousPlants function below.
def poisonousPlants(p):
    cntr = 0

    while True:
        del_list = []
        
        for i in range(1,len(p)):
            if p[i] > p[i-1]:
                del_list.append(i)
        if not del_list:
            return cntr
        else:
            cntr += 1
            for index in sorted(del_list, reverse=True):
                del p[index]



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
