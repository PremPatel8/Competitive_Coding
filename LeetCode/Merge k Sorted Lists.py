from typing import List
from queue import PriorityQueue

"""
Problem Name: Merge k Sorted Lists

Problem Section: Linked List

Problem Statement:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

Resources:
"""

""" 133 / 133 test cases passed.
	Status: Accepted
Runtime: 164 ms
Memory Usage: 17.5 MB """

# Solution techniques are:
# Brute Force single list sort,          T - O(Nlog⁡N), S - O(N) , where N is the total number of nodes.
# Compare one by one each LL's head ptr, T - O(kN), S - O(n) / O(1), where k is the number of linked lists.
# Optimize Approach 2 by Priority Queue, T - O(N log⁡ k), S - O(n) / O(k) - BEST
# Merge lists one by one,                T - O(kN), S - O(1)
# Merge with Divide And Conquer,         T - O(N log ⁡k), S - O(1) - BEST

# Time complexity : O() Space complexity : O() Optimize Approach 2 by Priority Queue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     no_lists = len(lists)
    #     pqueue = PriorityQueue(maxsize=no_lists)
    #     dummy = ListNode(None)
    #     curr = dummy

    #     for list_idx, node in enumerate(lists):
    #         if node:
    #             pqueue.put((node.val, list_idx, node))

    #     while pqueue:
    #         poped = pqueue.get()
    #         list_idx = poped[1]
    #         curr.next = poped[2]
    #         curr = curr.next

    #         if curr.next:
    #             pqueue.put((curr.next.val, list_idx, curr.next))

    #     return dummy.next

    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next


myobj = Solution()
# inpt = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(myobj.mergeKLists(inpt))
