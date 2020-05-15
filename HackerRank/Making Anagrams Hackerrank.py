#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
	len_a = len(a)
	len_b = len(b)
	match_count = 0

	a_freq = {}

	b_freq = {}

	if a == b:
		return 0
	else:
		for x in a:
			if x in a_freq:
				a_freq[x] += 1
			else:
				a_freq[x] = 1
		for x in b:
			if x in b_freq:
				b_freq[x] += 1
			else:
				b_freq[x] = 1

		# print(a_freq)
		# print(b_freq)

		if len_a<len_b:
			smaller = a_freq
			larger = b_freq
		else:
			smaller = b_freq
			larger = a_freq

		for ki in smaller:
			if ki in larger:
				if larger[ki] == smaller[ki]:
					match_count += smaller[ki]
				else:
					match_count += smaller[ki] if smaller[ki] < larger[ki] else larger[ki]

		return ((len_a-match_count)+(len_b-match_count))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
