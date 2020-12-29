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
""" 
the solution for every index i is simply the product of all the values to the left of index i with all the values to the right of index i.
There are, of course, no values to the left of index 0 and no values to the right of index arr.length - 1, 
but in these cases we can conveniently use 1 which is neutral to multiplication.
"""

# Time complexity : O(n) Space complexity : O(n)


class Solution:
    def array_of_array_products(self, arr):
        if len(arr) == 1 or len(arr) == 0:
            return []

        output = []
        product = 1

        # Calculate the prefix product array for all values to the left of index not including the value at index,
        # since there are no values to the left of index 0, hence we use 1
        for i in range(len(arr)):
            output.append(product)
            product = product * arr[i]

        # output = [1, 8, 80] (Prefix Product array)
        product = 1

        # Calculate the postfix product values for all the values to the right of index and not including inec value.
        # and directly multiply them to the prefix prod array values to get final output
        # output = [20, 2, 1] (Postfix Product array example)
        for i in range(len(arr)-1, -1, -1):
            output[i] = product * output[i]
            product = product * arr[i]

        return output


myobj = Solution()
arr = [8, 10, 2]
# Prefix Product array = [1, 8, 80]
# Postfix Product array = [20, 2, 1]
# op = [20, 16, 80]
print(myobj.array_of_array_products(arr))
