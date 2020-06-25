class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = len(s)
        maxoutput = 0
        ptr1 = ptr2 = 0
        index = [0]*26

        while ptr2 < strLen:
            ptr1 = max(ptr1, index[ord(s[ptr2])-ord('a')])

            maxoutput = max(maxoutput, ptr2-ptr1+1)

            index[ord(s[ptr2])-ord('a')] = ptr2+1

            ptr2 += 1

        return maxoutput


myObj = Solution()
# inpt = "abcabcbb"
inpt = "bacabcbb"
print(myObj.lengthOfLongestSubstring(inpt))
