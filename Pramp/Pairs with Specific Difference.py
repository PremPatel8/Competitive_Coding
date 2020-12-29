from typing import List

"""
Problem Name: Pairs with Specific Difference (2 sum / 2 diff)

Problem URL: 

Problem Section: 

Problem Statement:
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array

Resources:

runtime: 

"""

# Solution techniques are

# Time complexity : O() Space complexity : O()


""" def find_pairs_with_given_difference(arr, k):
  seen = {}
  res = []
  #arr.sort()
  arrSet = set(arr)
  
  for i, no in enumerate(arr):
    com = no-k
    
    seen[com] = no
  
  print(seen)
  
  for key in arr:
    if key in seen:
      res.append([seen[key],key])
  
  return res """

""" 
x - y = k
x = k + y
y = x - k
"""


def find_pairs_with_given_difference(arr, k):
    comNum = {}  # aka yNum
    res = []

    for no in arr:
        comNum[no-k] = no

    for y in arr:
        if y in comNum:
            res.append([comNum[y], y])

    return res


def find_pairs_with_given_difference(arr, k):
    arrSet = set(arr)
    out = []

    for elem in arr:
        if k + elem in arrSet:
            out.append([k + elem, elem])
    return out


arr = [0, -1, -2, 2, 1]
k = 1
# output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

print(find_pairs_with_given_difference(arr, k))

# tinutomson@gmail.com
# tinutomson@yahoo.com
