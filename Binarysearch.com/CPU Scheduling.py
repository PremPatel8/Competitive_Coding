""" Intuition

The key here is to sort the tasks by their start time, and "sort" the heap by the duration. The heap contains all the tasks that are able to start (past our current time).
Implementation

The time variable keeps track of the current time I'm at. Every time I get my next task, I add its duration to the time. The time starts at the earliest task, which is tasks[0] after sorting. Iterate through all the tasks, adding all the tasks to the heap that are <= to our current time. (aka they are able to be scheduled). The heap "sorts" the tasks by their duration. The heap doesn't care about their starting time, only the duration, as tasks are only added to the heap if they are able to start.

The "if not heap" line is for when there is a break in the task times. For ex, if you have a tasks [1,1,5] and [2,9,2], there is going to be a break between time 6 and 9, so "short circuit"/jump the time to the next available time. Doing time += 1 there is too slow.
Time Complexity

O(nlog⁡(n))\mathcal{O}(n\log(n))O(nlog(n)) This is nlogn to sort the list as well as to add and remove every task from the heap.
Space Complexity

O(n)\mathcal{O}(n)O(n) Linear space to store the heap.
 """
import heapq
from queue import PriorityQueue


class Solution:
    # 584 milliseconds — faster than 66.67% in Python
    """ def solve(self, tasks):
        tasks.sort(key=lambda x: (x[1], x[2], x[0]))
        idx = 0
        time = tasks[0][1]
        heap = []
        res = []

        heapq.heapify(heap)

        while idx < len(tasks):
            while idx < len(tasks) and tasks[idx][1] <= time:
                heapq.heappush(heap, (tasks[idx][2], tasks[idx][0]))
                idx += 1
            if not heap:
                time = tasks[idx][1]
                continue
            dur, ID = heapq.heappop(heap)
            res.append(ID)
            time += dur
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res """

    # 2321 milliseconds — faster than 1.33% in Python
    # 1568 milliseconds — faster than 5.33% in Python
    # 2291 milliseconds — faster than 1.33% in Python
    def solve(self, tasks):
        tasks.sort(key=lambda x: (x[1], x[2], x[0]))
        idx = 0
        time = tasks[0][1]
        pq = PriorityQueue()
        res = []

        while idx < len(tasks):
            while idx < len(tasks) and tasks[idx][1] <= time:
                pq.put((tasks[idx][2], tasks[idx][0]))
                idx += 1
            if pq.empty():
                time = tasks[idx][1]
                continue
            dur, ID = pq.get()
            res.append(ID)
            time += dur

        while not pq.empty():
            res.append(pq.get()[1])

        return res


# input [id, queue_time, duration]
# tasks = [
#     [0, 1, 5],
#     [1, 1, 5],
#     [2, 2, 2]
# ]

# expected output
# [0, 2, 1]

# input
tasks = [
    [0, 2, 0],
    [1, 2, 0],
    [2, 3, 1],
    [3, 1, 0]
]

# expected output
# [3, 0, 1, 2]

# actual output
myobj = Solution()

print(myobj.solve(tasks))
