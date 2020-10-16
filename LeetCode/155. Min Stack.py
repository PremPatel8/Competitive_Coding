from typing import List

"""
Problem Name: 155. Min Stack

Problem URL: https://leetcode.com/problems/min-stack/

Problem Section: Stack, Design

Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Resources:
https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution

runtime: 
18 / 18 test cases passed.
	Status: Accepted
Runtime: 52 ms
Memory Usage: 18.3 MB

"""

# Solution techniques are Storing current minimum with

# Time complexity : O(1) Space complexity : O(n)


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        curMin = self.getMin()

        if curMin == None or x < curMin:
            curMin = x

        self.stack.append((x, curMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
