from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


myObj = Solution()
# inpt = ["eat", "tea", "tan", "ate", "nat", "bat"]
inpt = ["eat", "tea", "tan", "tea", "ate", "nat", "bat"]
# inpt = ["", ""]
# inpt = ["tea", "tea"]

print(myObj.groupAnagrams(inpt))
