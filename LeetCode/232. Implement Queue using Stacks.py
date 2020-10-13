from typing import List

"""
Problem Name: 232. Implement Queue using Stacks

Problem URL: https://leetcode.com/problems/implement-queue-using-stacks/

Problem Section: Stack, Queue, List

Problem Statement:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.


Resources:

runtime: 
20 / 20 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14.2 MB

"""

""" Solution techniques are use two stacks / lists, one stack is the input stack and one as output stack, 
push values to input stack, pop or peek values from the output stack, if at any point output stack is empty 
pop all values from input stack and push to output stack first, then pop or peek from output stack """

# Time complexity : Push O(1), Pop O(n) Space complexity : O(n)


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                tmp = self.in_stack.pop()
                self.out_stack.append(tmp)
            return self.out_stack.pop()
        else:
            return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                tmp = self.in_stack.pop()
                self.out_stack.append(tmp)
            return self.out_stack[-1]
        else:
            return self.out_stack[-1]

    def empty(self) -> bool:
        if not self.in_stack and not self.out_stack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
output = []
obj = MyQueue()
output.append(None)
output.append(obj.push(1))
output.append(obj.push(2))
output.append(obj.peek())
output.append(obj.pop())
output.append(obj.empty())
print(output)
