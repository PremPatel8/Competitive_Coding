from typing import List
from collections import OrderedDict

"""
Problem Name: 387. First Unique Character in a String

Problem Section: HashTable, String

Problem Statement:
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Example:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.

Resources:

"""

""" runtime """

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n) Using OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        if len(s) == 1:
            return 0

        ordered_dict = OrderedDict()

        for idx, ch in enumerate(s):
            if ch in ordered_dict:
                ordered_dict[ch][1] += 1
            else:
                ordered_dict[ch] = [idx, 1]

        for pstn, cnt in ordered_dict.values():
            if cnt == 1:
                return pstn

        return -1


myobj = Solution()
inpt = "loveleetcode"
print(myobj.firstUniqChar(inpt))
