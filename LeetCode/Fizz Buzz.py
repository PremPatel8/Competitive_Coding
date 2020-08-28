from typing import List

"""
Problem Name: Fizz Buzz

Problem Section: Math

Problem Statement:
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

Resources:

"""
""" 8 / 8 test cases passed.
	Status: Accepted
Runtime: 40 ms
Memory Usage: 14.9 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) Iterative String Concatenation solution


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []

        for num in range(1, n+1):
            res = ""
            if num % 3 == 0:
                res += "Fizz"
            if num % 5 == 0:
                res += "Buzz"

            if not res:
                res = str(num)

            output.append(res)

        return output


myobj = Solution()
inpt = 15
print(myobj.fizzBuzz(inpt))
