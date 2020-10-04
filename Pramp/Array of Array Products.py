from typing import List

"""
Problem Name: Array of Array Products

Problem Section: 

Problem Statement:
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.
Solve without using division and analyze your solution’s time and space complexities.

Example:
input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]

Constraints:
[time limit] 5000ms

[input] array.integer arr
    0 ≤ arr.length ≤ 20

[output] array.integer

Resources:
"""

""" runtime """

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n)


class Solution:
    def array_of_array_products(self, arr):
        if len(arr) == 1 or len(arr) == 0:
            return []

        output = []
        product = 1

        for i in range(len(arr)):
            output.append(product)
            product = product * arr[i]

        product = 1

        for i in range(len(arr)-1, -1, -1):
            output[i] = output[i] * product
            product = product * arr[i]

        return output


myobj = Solution()
arr = [8, 10, 2]
print(myobj.array_of_array_products(arr))
