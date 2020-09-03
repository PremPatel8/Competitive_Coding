from typing import List

"""
Problem Name: Factorial Trailing Zeroes

Problem Section: Math

Problem Statement:
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.


Resources:

"""

""" 502 / 502 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14.1 MB """

# Solution techniques are
# Time complexity : O(log n) Space complexity : O(1) div by 5 solution
""" 
The ZERO comes from 10.
The 10 comes from 2 x 5
And we need to account for all the products of 5 and 2. likes 4×5 = 20 ...
So, if we take all the numbers with 5 as a factor, we'll have way more than enough even numbers to pair with them to get factors of 10
 """


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        while n != 0:
            n = n // 5
            count += n

        return count


myobj = Solution()
inpt = 20
print(myobj.trailingZeroes(inpt))
