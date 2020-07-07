# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """ common approach """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        currA, currB = headA, headB

        while currA is not currB:
            currA = currA.next if currA else headB

            currB = currB.next if currB else headA

        return currA

    """ Alt approach 1 """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        currA, currB = headA, headB
        exists_set = set()
        
        while currA:
            exists_set.add(currA)
            currA = currA.next

        while currB:
            if currB in exists_set:
                return currB
            currB = currB.next
            
        return None

    """ Alt approach 2 """
    def getLength(self, node):
        n = 0
        
        while node:
            n += 1 #add one
            node = node.next
        return n
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Our approach here is to go through each LL and determine its size.
        1. As these lists must intersect at some point, if they are coupled,
         the intersection point MUST be at least the length of the shorter list
        2. Dump all nodes in the larger node until we have parity
        3. Finally, advance the nodes one at a time until/if we find the intersect
        """
        nA = self.getLength(headA)
        nB = self.getLength(headB)
        
        if not nA or not nB:
            return None # No intersection possible
        
        #Dump off excess values
        if nA > nB:
            while nA != nB:
                headA = headA.next
                nA -= 1
        elif nA < nB:
            while nA != nB:
                headB = headB.next
                nB -= 1
        
        while headA: # While we still have items
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        #We got to the end with no issues
        return None