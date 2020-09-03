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
# Time complexity : O(n log n) Space complexity : O(n log n) Set solution
""" Let S be any finite set, f be any function from S to itself, and x0 be any element of S. 
For any i > 0, let xi = f(xi − 1). Let μ be the smallest index such that the value xμ reappears infinitely often within the sequence of values xi, 
and let λ (the loop length) be the smallest positive integer such that xμ = xλ + μ. The cycle detection problem is the task of finding λ and μ. """


class Solution:
    def isHappy(self, n: int) -> bool:
        squareSet = set()

        squareSum = lastDigit = 0

        while (n not in squareSet):
            squareSet.add(n)
            squareSum = 0

            while n > 0:
                lastDigit = n % 10
                squareSum += lastDigit*lastDigit
                n = n // 10

            if squareSum == 1:
                return True
            else:
                n = squareSum

        return False


myobj = Solution()
inpt = 19
print(myobj.isHappy(inpt))
