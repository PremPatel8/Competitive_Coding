#!/bin/python3

import math
import os
import random
import re
import sys
import copy
import bisect
from statistics import median


# Complete the activityNotifications function below.

def find_median(f,p):
    # print("")
    # print(f"p = {p}")
    # print(f"freq array = {f}")

    cumulative = 0
    p += 1

    # print(f"p after = {p}")

    for i in range(len(f)):
        # print(f"f[{i}] = {f[i]}")
        # print(f"cumulative before = {cumulative}")

        cumulative += f[i]

        # print(f"cumulative after = {cumulative}")

        if cumulative == p:
            # print(f"mdn calculated = {i}")
            return i
        elif cumulative > p:
            # print(f"mdn calculated_1 = {i}")
            return i

    # print("end")


def activityNotifications(expenditure, d):
    notification = 0
    expenditure_freq = [0] * 201
    mdn = 0

    for x in expenditure[:d]:
        expenditure_freq[x] += 1

    # print(expenditure_freq)

    for itr, val in enumerate(expenditure[d:], start=d):
        # print(f"val start = {val}")

        if d % 2 == 0:
            # EVEN find the element at floor((N-1)/2) and floor(N/2) th position and return their average.
            mdn =  find_median(expenditure_freq, math.floor((d-1) / 2)) + find_median(expenditure_freq, math.floor(d / 2))
        else:
            # ODD find the element at floor(N/2)-th place and median is that element.
            mdn = find_median(expenditure_freq, math.floor(d / 2)) * 2


        if val >= mdn:
            print(f"val = {val}, mdn = {mdn}, {val >= mdn}")

        if val >= mdn:
            notification += 1
            # print(f"notification = {notification}")

        popVal = expenditure[itr - d]

        expenditure_freq[popVal] = max(0, expenditure_freq[popVal]-1)

        expenditure_freq[val] += 1

    return notification


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(f"result = {result}")

# fptr.write(str(result) + '\n')

# fptr.close()
