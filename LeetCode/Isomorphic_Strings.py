from typing import List

"""
Problem Name: Isomorphic Strings


Problem URL: https://leetcode.com/problems/isomorphic-strings/description/

Problem Section: Hash Table, Dict, String

Problem Difficulty: Easy to Medium

Problem Statement:
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.

No two characters may map to the same character, but a character may map to itself.

Resources:

"""


class Solution:
    """
    Solution technique: Character Mapping with Dictionary / HashMap

    Time & Space Complexity:
    Time: O(n)
    Space: O(1) since the size of the ASCII character set is fixed

    Runtime: 37 ms
    Memory: 14.2 MB
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):

            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True

    """
    Solution technique: Character Mapping with Lists of fixed size (ASCII size)

    Time & Space Complexity:
    Time: O(n)
    Space: O(1) since the size of the ASCII character set is fixed

    Runtime: 46 ms
    Memory: 14.3 MB
    """

    def isIsomorphic1(self, s: str, t: str) -> bool:
        mapping_s_t = [0]*256
        mapping_t_s = [0]*256

        for c1, c2 in zip(s, t):

            # Case 1: No mapping exists in either of the dictionaries
            if (mapping_s_t[ord(c1)] == 0) and (mapping_t_s[ord(c2)] == 0):
                mapping_s_t[ord(c1)] = c2
                mapping_t_s[ord(c2)] = c1

            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both
            elif mapping_s_t[ord(c1)] != c2 or mapping_t_s[ord(c2)] != c1:
                return False

        return True

    """
    Solution technique: transformation using 2 Arrays / lists of size 256 (ASCII size)

    The idea is that we need to map a char to another one, for example, "egg" and "add", 
    we need to constract the mapping 'e' -> 'a' and 'g' -> 'd'. Instead of directly mapping 'e' to 'a', 
    another way is to mark them with same value, for example, 'e' -> 1, 'a'-> 1, and 'g' -> 2, 'd' -> 2, this works same.
    So we use two arrays here m1 and m2, initialized space is 256 (Since the whole ASCII size is 256, 128 also works here). 
    Traverse the character of both s and t on the same position, 
    if their mapping values in m1 and m2 are different, means they are not mapping correctly, return false; 
    else we construct the mapping, since m1 and m2 are both initialized as 0, 
    we want to use a new value when i == 0, so i + 1 works here.

    Time & Space Complexity:
    Time: O(n)
    Space: O(1)

    Runtime: 59 ms
    Memory: 14.2 MB
    """

    def isIsomorphic2(self, s: str, t: str) -> bool:
        m1 = [0]*256
        m2 = [0]*256

        # ord() function returns an integer representing the Unicode character.
        for idx in range(len(s)):
            if m1[ord(s[idx])] != m2[ord(t[idx])]:
                return False

            m1[ord(s[idx])] = idx + 1
            m2[ord(t[idx])] = idx + 1

        return True

    """
    Solution technique: First occurence transformation

    Time & Space Complexity:
    Time: O(n)
    Space: O(n) We form two new strings returned by our transformation function. 
    The size of ASCII character set is fixed and the keys in our dictionary are valid ASCII characters only. 
    So the size of the map in the transform function doesn't contribute to the space complexity.

    Runtime: 63 ms
    Memory: 16.5 MB
    """

    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))

        return " ".join(new_str)

    def isIsomorphic3(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)


myobj = Solution()
s = "egg"
t = "add"
# print(myobj.isIsomorphic(s, t) == True)

# print(myobj.isIsomorphic1(s, t) == True)

# print(myobj.isIsomorphic2(s, t) == True)

print(myobj.isIsomorphic3(s, t) == True)
