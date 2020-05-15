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


def activityNotifications(expenditure, d):
    flag = 0
    notification = 0
    tmp_expenditure = []

    for itr, val in enumerate(expenditure[d:], start=d):

        if flag == 0:
            # print("in flag 0")
            tmp_expenditure = copy.copy(expenditure[itr-d:itr])
            tmp_expenditure.sort()
            flag = 1

        if d % 2 == 0:
            median1 = tmp_expenditure[d // 2]
            median2 = tmp_expenditure[d // 2 - 1]
            mdn = (median1 + median2)
        else:
            mdn = 2 * tmp_expenditure[d // 2]

        # mdn = median(tmp_expenditure)

        if val >= mdn:
            notification += 1

        popVal = expenditure[itr-d]
        tmp_expenditure.remove(popVal)
        bisect.insort(tmp_expenditure, val)
        # tmp_expenditure.append(val)

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
