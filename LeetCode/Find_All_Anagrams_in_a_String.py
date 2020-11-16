from typing import List
from collections import Counter, defaultdict

"""
Problem Name: 438. Find All Anagrams in a String

Problem URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/

Problem Section:

Problem Statement:
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Resources:
https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/636988/Sliding-Window-or-HashTable-or-Java-Explained-with-Diagram-Beats-99

runtime:

"""

# Solution techniques are

# Time complexity : O(S) Space complexity : O(1)
""" Time Complexity - O(S)
Each array element element would be traversed at most twice . First time by windowEnd to decrement the value, then by windowStart to increment . Best case would be when none of the array elements are part of anagram.
eg - P = 'abc' S = 'xyzr' . Here, both windowEnd and windowStart would be incremented at same time.

Space complexity - O(1)
Since we are using constant extra space (map) of size 26 / Dict used by me but at max there will be 26 keys for each alphabet in the dict"""

""" Question - How are we checking for valid anagrams without actually traversing over map
The idea is that window Size (windowEnd-windowStart) would only we equal to length of P when all the characters in window are valid anagram. (Point 3 above).
Example - P = aab S = aaabca. Here, map = [ 'a' = 2, 'b' = 1].

After traversing first 2 a's aa in S, map = ['a' = 0, 'b' = 1], window = aa.
Now when we traverse 3rd a (aaa) in S, map count for 'a' is 0. So we know window is no longer valid anagram of P, and we increment start, now window has a only.
See how we are reducing window size here when we dont find right anagram character In this example, window size would be only equal to 3, when it has characters a,a and b.
Feel free to ask questions in comments. Do upvote if you understood the solution.
 """


class Solution:
    """ def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            # This step is O(1), since there are at most 26 English letters
            if sCounter == pCounter:
                res.append(i-len(p)+1)   # append the starting index
            # decrease the count of oldest char in the window
            sCounter[s[i-len(p)+1]] -= 1
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = defaultdict(int)
        result = []

        for chr in p:
            p_dict[chr] += 1

        start = end = 0

        while end < len(s):
            if s[end] in p_dict and p_dict[s[end]] > 0:
                p_dict[s[end]] -= 1
                end += 1

                if end-start == len(p):
                    result.append(start)

            elif start == end:
                start += 1
                end += 1
            else:
                p_dict[s[start]] += 1
                start += 1

        return result


""" myobj = Solution()
s = "cbaebabacd"
p = "abc"
print(myobj.findAnagrams(s, p)) """
