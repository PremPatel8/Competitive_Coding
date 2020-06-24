class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr1 = ptr2 = 0
        uniqueChr = set()
        maxoutput = 0

        while ptr2 < len(s):
            if s[ptr2] not in uniqueChr:
                uniqueChr.add(s[ptr2])
                ptr2+=1
                maxoutput = max(maxoutput, len(uniqueChr))
            else:
                uniqueChr.remove(s[ptr1])
                ptr1+=1
        
        return maxoutput




myObj = Solution()
# inpt = "abcabcbb"
inpt = "bacabcbb"
print(myObj.lengthOfLongestSubstring(inpt))
