#!/bin/python3

import os
import sys

#
# Complete the bonetrousle function below.
#
def bonetrousle(n, k, b):
    # print()

    min = b*(b+1)//2
    max = b*(2*k-b+1)//2

    # print(f"min, max = {min, max}")

    if not(n <= max and n >= min):
        return ["-1"]
        
    else:
        total = 0

        i = 1

        sol = []

        sol = list(range(1,b+1))

        # print(f"sol = {sol}")

        total = sum(sol)

        while total != n:
            if sol[b-i] < k-i+1:
                total = 0

                sol[b-i] += 1

                total = sum(sol)
            else:
                i += 1

        return sol



                

        
            

if __name__ == '__main__':

    t = int(input())

    print(f"t = {t}")

    for t_itr in range(t):
        print()
        print(f"t_itr = {t_itr}")
        nkb = input().split()

        n = int(nkb[0])

        k = int(nkb[1])

        b = int(nkb[2])

        print(f"n,k,b = {n,k,b}")

        result = bonetrousle(n, k, b)

        print(f"result = {result}")

        print(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
