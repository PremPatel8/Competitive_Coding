# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            oddPtr = head
        else:
            return head
        if head.next:
            evenPtr = head.next
        else:
            return head

        oddHead = evenHead = None

        while oddPtr or evenPtr:
            if oddPtr:
                if not oddHead:
                    oddHead = oddPtr
                    oddCur = oddPtr
                else:
                    oddCur.next = oddPtr
                    oddCur = oddCur.next

                if oddPtr.next:
                    oddPtr = oddPtr.next.next
                else:
                    oddPtr = None

            if evenPtr:
                if not evenHead:
                    evenHead = evenPtr
                    evenCur = evenPtr
                else:
                    evenCur.next = evenPtr
                    evenCur = evenCur.next

                if evenPtr.next:
                    evenPtr = evenPtr.next.next
                else:
                    evenPtr = None

        evenCur.next = None
        oddCur.next = evenHead

        return oddHead
