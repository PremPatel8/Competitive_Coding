# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list. 
You may assume the two numbers do not contain any leading zero, except the number 0 itself. """

""" Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         numA = numB = total = 0
#         headA = l1
#         headB = l2
#         head = tail = None

#         numA = self.getNum(headA)
#         numB = self.getNum(headB)

#         total = numA + numB

#         if total == 0:
#             return ListNode(0)

#         while total > 0:
#             digit = total % 10

#             if not head:
#                 head = tail = ListNode(digit)
#             else:
#                 tail.next = ListNode(digit)
#                 tail = tail.next

#             total = total//10

#         return head

#     def getNum(self, headPtr):
#         num = i = 0
#         while headPtr:
#             num += headPtr.val * 10**i
#             headPtr = headPtr.next
#             i += 1

#         return num

""" LeetCode Solution """
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        head=None
        while(l1 or l2):
            node1val= l1.val if l1 else 0
            node2val = l2.val if l2 else 0
            ans = node1val + node2val
            if carry: ans = ans + carry
            if ans >= 10: 
                carry = 1
                ans = ans-10
            else:
                carry = 0
            newnode = ListNode(ans)
            if not head:
                head = newnode
                newnode.next = None
                current = head
            else:                
                newnode.next = None
                current.next = newnode
                current = newnode
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry:
            newnode = ListNode(carry)
            newnode.next = None
            current.next = newnode
            current = newnode
        return head


h1 = ListNode(2)
h1.next = ListNode(4)
h1.next.next = ListNode(3)

h2 = ListNode(5)
h2.next = ListNode(6)
h2.next.next = ListNode(4)

myobj = Solution()

print(myobj.addTwoNumbers(h1, h2))
