#!/bin/python3

import math
import os
import random
import re
import sys
import math

# Complete the primality function below.


def primality(n):
    if n < 2:
        return "Not prime"
    elif n <= 3:
        return "Prime"
    elif n % 2 == 0 or n % 3 == 0:
        return "Not prime"
    else:
        upperLimit = int(math.sqrt(n)+1)

        for i in range(5, upperLimit, 2):
            if n % i == 0:
                return "Not prime"

    return "Prime"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())
    result = []

    for p_itr in range(p):
        n = int(input())

        result.append(primality(n))

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
