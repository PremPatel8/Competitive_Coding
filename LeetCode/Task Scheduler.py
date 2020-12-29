from typing import List
from collections import Counter
from heapq import heappush, heappop

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
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/826/discuss/130786/Python-solution-with-detailed-explanation

runtime: 
71 / 71 test cases passed.
	Status: Accepted
Runtime: 616 ms
Memory Usage: 14.9 MB
"""

# Solution techniques are
# The main idea is to schedule the most frequent tasks as frequently as possible.

# Time complexity : O() Space complexity : O()
"""
The main idea is to schedule the most frequent tasks as frequently as possible. Begin with scheduling the most frequent task. Then cool-off for n, and in that cool-off period schedule tasks in order of frequency, or if no tasks are available, then be idle.
Exampe: Say we have the following tasks: [A,A,A,B,C,D,E] with n =2
Now if we schedule using the idea of scheduling all unique tasks once and then calculating if a cool-off is required or not, then we have: A,B,C,D,E,A,idle,dile,A i.e. 2 idle slots.
But if we schedule using most frequent first, then we have:
2.1: A,idle,idle,A,idle,idle,A
2.2: A,B,C,A,D,E,A i.e. no idle slots. This is the general intuition of this problem.
3.The idea in two can be implemented using a heap and temp list. This is illustrated in the code below.
4.Time complexity is O(N * n) where N is the number of tasks and n is the cool-off period.
5.Space complexity is O(1) - will not be more than O(26).
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curr_time, heap = 0, []

        # Python only has min heap so making the frequency negative before
        # pushing to heap ensures that the highest frequency will be at the top.
        for task, freq in Counter(tasks).items():
            heappush(heap, (-1*freq, task))

        while heap:
            i, temp = 0, []

            while i <= n:
                curr_time += 1
                if heap:
                    freq, task = heappop(heap)
                    if freq != -1:
                        temp.append((freq+1, task))
                if not heap and not temp:
                    break
                else:
                    i += 1

            for item in temp:
                heappush(heap, item)

        return curr_time


myobj = Solution()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
# Output: 8
print(myobj.leastInterval(tasks, n))
