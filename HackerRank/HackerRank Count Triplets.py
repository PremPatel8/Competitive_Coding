#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    cntr = 0

    arr_dict = {}

    for x in arr:
        if x in arr_dict:
            arr_dict[x] += 1
        else:
            arr_dict[x] = 1

    print(f"arr_dict = {arr_dict}")

    for x in sorted(arr_dict.keys()):
        print(f"x = {x}")
        if x * r in arr_dict and x * r * r in arr_dict:

            if len(arr_dict.keys()) == 1:
                print("Here")
                n = arr_dict[x]
                r = 3

                print(f"math.factorial({n}) // math.factorial({(n - r)}) // math.factorial({r}) = {math.factorial(n) // math.factorial((n - r)) // math.factorial(r)}")

                cntr += math.factorial(n) // math.factorial((n - r)) // math.factorial(r)

            elif r == 1:
                if arr_dict[x] >= 3:
                    cntr += math.factorial(arr_dict[x])

            else:
                print(f"math.factorial(arr_dict[{x}])*math.factorial(arr_dict[{x * r}])*math.factorial(arr_dict[{x * r * r}]) = {math.factorial(arr_dict[x]) * math.factorial(arr_dict[x * r]) * math.factorial(arr_dict[x * r * r])}")
                print(f"math.factorial({arr_dict[x]})*math.factorial({arr_dict[x * r]})*math.factorial({arr_dict[x * r * r]})")

                cntr += math.factorial(arr_dict[x]) * math.factorial(arr_dict[x * r]) * math.factorial(arr_dict[x * r * r])
        else:
            break

    return cntr


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(f"ans = {ans}")

    # fptr.write(str(ans) + '\n')

    # fptr.close()
