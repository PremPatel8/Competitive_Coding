#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.


def activityNotifications(expenditure, d):
    expenditure.sort()

    i = 0
    median = 0
    idx = 0
    idx1 = 0
    notification = 0

    for itr, val in enumerate(expenditure):
        if itr < d:
            continue

        if d // 2 != 0:
            idx = ((d + 1) // 2) - 1 + i
            median = expenditure[idx]
        else:
            idx = d + 1 // 2 - 1 + i
            idx1 = idx + 1
            median = (expenditure[idx] + expenditure[idx1]) // 2

        if expenditure[itr] >= 2 * median:
            notification += 1

        i += 1

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
