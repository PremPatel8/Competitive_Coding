from typing import List

"""
Problem Name: Task Scheduler

Problem URL: https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/826/

Problem Section: Others

Problem Statement:
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Constraints:
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].

Resources:


runtime: 

"""

# Solution techniques are
# The main idea is to schedule the most frequent tasks as frequently as possible.

# Time complexity : O() Space complexity : O()


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass


myobj = Solution()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(myobj.leastInterval(tasks, n))
