# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        headOdd = ListNode(0)
        curodd = headOdd
        headEven = ListNode(0)
        cureven = headEven
        isOdd = True
        while head:
            if isOdd:
                curodd.next = head
                curodd = curodd.next
            else:
                cureven.next = head
                cureven = cureven.next
            isOdd = not isOdd
            head = head.next
        curodd.next = headEven.next
        cureven.next = None
        return headOdd.next
