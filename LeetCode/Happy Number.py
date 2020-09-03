from typing import List

"""
Problem Name: Happy Number

Problem Section: Math

Problem Statement:
Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Resources:

"""

""" 401 / 401 test cases passed.
	Status: Accepted
Runtime: 36 ms
Memory Usage: 13.9 MB """

# Solution techniques are Set, Floyd Cycle detection algorithm,
# Time complexity : O(λ + μ) Space complexity : O() Floyd Cycle detection algorithm
""" Let S be any finite set, f be any function from S to itself, and x0 be any element of S. 
For any i > 0, let xi = f(xi − 1). Let μ be the smallest index such that the value xμ reappears infinitely often within the sequence of values xi, 
and let λ (the loop length) be the smallest positive integer such that xμ = xλ + μ. The cycle detection problem is the task of finding λ and μ. """


class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSquareSum(n):
            return sum(int(i) ** 2 for i in str(n))

        slow = digitSquareSum(n)
        fast = digitSquareSum(digitSquareSum(n))

        while slow != fast:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(digitSquareSum(fast))

        return fast == 1


myobj = Solution()
inpt = 20
print(myobj.isHappy(inpt))
