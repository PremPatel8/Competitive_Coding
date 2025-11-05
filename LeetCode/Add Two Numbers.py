
""" You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list. 
You may assume the two numbers do not contain any leading zero, except the number 0 itself. """

""" Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. """


from typing import Optional

"""
Elementary Math solution

Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

Space complexity : O(1). The length of the new list is at most max(m,n)+1 However, we don't count the answer as part of the space complexity.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummyHead = ListNode()
        carry = 0

        while l1 or l2 or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            columnSum = l1Val + l2Val + carry

            carry = columnSum // 10
            
            newNode = ListNode(columnSum % 10)

            curr.next = newNode
            curr = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        

        return dummyHead.next


h1 = ListNode(2)
h1.next = ListNode(4)
h1.next.next = ListNode(3)

h2 = ListNode(5)
h2.next = ListNode(6)
h2.next.next = ListNode(4)

myobj = Solution()

print(myobj.addTwoNumbers(h1, h2))
