#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    sum_of_digits = sum(int(digit) for digit in n) 
    sum_of_digits *= k
    
    if sum_of_digits <= 9:
        return sum_of_digits
    else:
        return superDigit(str(sum_of_digits),1)


if __name__ == '__main__':
    # s = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    print(result)

    # s.write(str(result) + '\n')

    # s.close()
