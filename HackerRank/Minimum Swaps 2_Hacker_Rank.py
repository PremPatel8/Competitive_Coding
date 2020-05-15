#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    cnt = 0
    min_idx = 0

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        cnt += 1

    return cnt


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)
