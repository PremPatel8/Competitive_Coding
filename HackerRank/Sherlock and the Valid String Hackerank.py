#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    s_freq = {}
    s_freq_1 = {}
    flag = ""

    for x in s:
        if x in s_freq:
            s_freq[x] += 1
        else:
            s_freq[x] = 1

    # print(s_freq)

    for itr_x in s_freq:
        if s_freq[itr_x] in s_freq_1:
            s_freq_1[s_freq[itr_x]] += 1
        else:
            s_freq_1[s_freq[itr_x]] = 1

    # print(s_freq_1)


    if len(s_freq_1.keys())>2:
        flag = "NO"
    elif len(s_freq_1.keys()) < 2:
        flag = "YES"
    elif s_freq_1[list(s_freq_1.keys())[1]] != 1:
        flag = "NO"
    # elif abs(list(s_freq_1.keys())[0]-list(s_freq_1.keys())[1]) != 1:
    #     flag = "NO"
    else:
        flag = "YES"
    
    return flag

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
