#!/bin/python3

from typing import List

"""
Problem Name: Maximum Subarray Sum

Problem URL: https://www.hackerrank.com/challenges/maximum-subarray-sum/problem?h_r=internal-search

Problem Section: search, array

Problem Difficulty: Hard

Problem Statement:
Given a n element array of integers 'a' and a integer 'm' determine the maximum value of the sum of any of its subarrays modulo 'm'

Example:
a = [1,2,3]
m = 2
the max modulus is 1

Resources:

"""

import math
import os
import random
import re
import sys
from collections import defaultdict
from itertools import accumulate

import bisect

# Complete the maximumSum function below.


def maximumSum(coll, m):
    n = len(coll)
    maxSum, prefixSum = 0, 0
    sortedPrefixes = []

    for endIndex in range(n):
        prefixSum = (prefixSum + coll[endIndex]) % m
        maxSum = max(maxSum, prefixSum)

        startIndex = bisect.bisect_right(sortedPrefixes, prefixSum)
        if startIndex < len(sortedPrefixes):
            maxSum = max(maxSum, prefixSum - sortedPrefixes[startIndex] + m)

        bisect.insort(sortedPrefixes, prefixSum)

    return maxSum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        print(f"result = {result}")

        # fptr.write(str(result) + '\n')

    # fptr.close()
