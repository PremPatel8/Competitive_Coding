#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.


def commonChild(s1, s2):
    s1_dict = {}
    s2_dict = {}

    cmnLtrs_s1 = []
    cmnLtrs_s2 = []

    count = 0

    cnt1 = 0
    cnt2 = 0
    mx1 = 0
    mx2 = 0

    for x in s1:
        if x not in s1_dict:
            s1_dict[x] = 1
        else:
            s1_dict[x] += 1

    for x in s2:
        if x not in s2_dict:
            s2_dict[x] = 1
        else:
            s2_dict[x] += 1

    print(s1_dict)
    print(s2_dict)

    for x in s1_dict.keys():
        if x in s2_dict:
            cmnLtrs_s1.append(x)

    if len(cmnLtrs_s1) == 0:
        return 0

    for x in s2_dict.keys():
        if x in s1_dict:
            cmnLtrs_s2.append(x)

    if len(cmnLtrs_s2) == 0:
        return 0

    print(f"cmnLtrs_s1 = {cmnLtrs_s1}")
    print(f"cmnLtrs_s2 = {cmnLtrs_s2}")

    for x in range(len(cmnLtrs_s1)):
        print(f"x = {x}")
        idx = x
        cnt1 = 0
        for y in s2:
            print(f"y = {y}, cmnLtrs_s1[{idx}] = {cmnLtrs_s1[idx]}")
            if y == cmnLtrs_s1[idx]:
                cnt1 += 1
                if idx < len(cmnLtrs_s1) - 1:
                    idx += 1
                else:
                    break

        if cnt1 > mx1:
            mx1 = cnt1

    for x in range(len(cmnLtrs_s2)):
    	print(f"x = {x}")
    	idx = x
    	cnt2 = 0
    	for y in s1:
    		print(f"y = {y}, cmnLtrs_s2[{idx}] = {cmnLtrs_s2[idx]}")
    		if y == cmnLtrs_s2[idx]:
    			cnt2 += 1
    			if idx < len(cmnLtrs_s2) - 1:
    				idx += 1
    			else:
    				break

    	if cnt2 > mx2:
    		mx2 = cnt2

    return mx1 if mx1 > mx2 else mx2


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
