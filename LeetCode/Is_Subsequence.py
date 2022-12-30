import bisect
from collections import defaultdict
from collections import deque
from typing import List

"""
Problem Name: Is Subsequence

Problem URL: https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1

Problem Section: 2 pointer, Binary Search, Stack
DP / Recursion + memoization ? 

Problem Difficulty: Easy

Problem Statement:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Resources:
https://leetcode.com/problems/is-subsequence/solutions/678389/python-3-solutions-dp-2-pointers-follow-up-bs-explained/
https://leetcode.com/problems/is-subsequence/solutions/1811547/3-Line-Solution-oror-Explanation-oror-O(n)-Time-and-O(1)-Space-Complexity/
https://leetcode.com/problems/is-subsequence/solutions/1811180/c-easy-3-approaches-brute-force-recursive-memoization/
https://leetcode.com/problems/is-subsequence/solutions/87264/easy-to-understand-binary-search-solution/
https://leetcode.com/problems/is-subsequence/solutions/87302/binary-search-solution-for-follow-up-with-detailed-comments/
"""


class Solution:
    """ Solution technique: 2 pointer

    Time & Space Complexity:
    Time: O(n + m) = O(n), because we traverse both strings only once.
    Space: O(1)

    Runtime: 43 ms
    Space: 13.9 MB
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

    """ Follow-up question: Binary Search sol
    Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
    and you want to check one by one to see if t has its subsequence. 
    In this scenario, how would you change your code?

    Time & Space Complexity:
    If we have a lot strings S1, S2, ... , Sk, where k is big number we want to find faster method. Let us create for each symbol sorted list of indexes for this symbol.

    Complexity, both time and space of preprocessing is O(n), we iterate once over our list.

    Complexity of one search for string S_i is O(m_i)*log(n), where m_i is length of string and we have log(n) factor, 
    because we potentially can have list of indexes with length n. So if m is the longest length of S_i, 
    we have complexity O(k m log n), when two-pointer approach has O(k n) complexity. 
    So, if length of original string n is big and m is small, it is worth it to use this method.

    Runtime: 34 ms
    Space: 14.4 MB

    Eg-1. s="abc", t="bahbgdca"

    posMap={
            b=[0,3],
            a=[1,7],

            # h=[2]
            # g=[4]
            # d=[5]

            c=[6]
            }

    i=0 ('a'): current_pstn=1 , move 1 position ahead = 2
    i=1 ('b'): current_pstn=3, move 1 position ahead = 4
    i=2 ('c'): current_pstn=6, move 1 position ahead = 7 (return true)

    Eg-2. s="abc", t="bahgdcb"
    posMap=[a={1}, b={0,6}, c={5}]
        i=0 ('a'): prev=1
        i=1 ('b'): prev=6
        i=2 ('c'): prev=? (return false) 
    """

    def isSubsequence_binary_search(self, s, t):
        posMap = defaultdict(list)

        # Don't want to do this in follow up question scenario because we will be dealing with multiple different s strings & 1 common t string
        # In that case it's better to just map out the entire t string once and then just compare all the s strings against that single map
        # provided java compiler is smart about caching the computed map to use between method calls, or input is changed to an array of s strings and 1 t string ?

        # s_char_set = set(s)
        # for idx, char in enumerate(t):
        #     # gives smaller map/dict saves space when size of t is large
        #     if char in s_char_set:
        #         posMap[char].append(idx)

        for idx, char in enumerate(t):
            posMap[char].append(idx)

        current_pstn = 0

        for ch in s:
            if ch not in posMap:
                return False

            charIndexList = posMap[ch]

            # Locate the insertion point for x in list a to maintain sorted order
            # If x is already present in a, the insertion point will be before (to the left of) any existing entries
            # If no element is smaller than x [i.e. x needs to be prepended to a] then it returns 0
            # If all elements are smaller than x [i.e. x doesn't fit in a, but needs to be appended to the end of it], it returns len(a)
            insertion_idx = bisect.bisect_left(charIndexList, current_pstn)

            # Situation where the current_pstn is ahead of the right most index inside charIndexList,
            # i.e. for given current_pstn, all valid index of the target char are to the left of current_pstn and hence subsequence property breaks
            if insertion_idx >= len(charIndexList):
                return False

            # Move the current_pstn ahead by 1 to so that next iteration checks the remaininng substring excluding current_pstn
            current_pstn = charIndexList[insertion_idx] + 1

        return True

    """ Solution technique: stack sol

    Time & Space Complexity:
    Time: O(n^2) ?
    Space: O(n), n is the size of string s, which is 0 <= s.length <= 100, so it's more like O(1) ?

    Runtime: 37 ms
    Space: 13.9 MB
    """

    def isSubsequence_stack(self, s: str, t: str) -> bool:
        my_stack = deque()

        for ch in s:
            my_stack.append(ch)

        idx = len(t)-1

        while idx >= 0 and len(my_stack) > 0:
            if t[idx] == my_stack[-1]:
                my_stack.pop()

            idx -= 1

        return len(my_stack) == 0

    """ Solution technique: recursion

    Time & Space Complexity:
    Time: 
    Space:

    Runtime:
    Space: 
    """

    def isSubsequence_recursion(self, s: str, t: str) -> bool:
        pass


myobj = Solution()
s = "abc"
t = "ahbgdc"
opt = True
print(myobj.isSubsequence_stack(s, t) == opt)
