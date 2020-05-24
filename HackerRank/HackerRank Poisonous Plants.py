#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# This solution works but is too slow
# Complete the poisonousPlants function below.
def poisonousPlants(p):
    stack_list = []

    for i in range(1, len(p)):
        if 




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
