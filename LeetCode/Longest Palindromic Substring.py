
class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = start = end = 0
        strlen = len(s)

        if not s or len(s) < 1:
            return ''

        while i < strlen:
            len1 = self.max_substr_len(s, i, i)
            len2 = self.max_substr_len(s, i, i+1)

            substrlen = max(len1, len2)

            if substrlen > end-start:
                start = i - ((substrlen-1)//2)
                end = i + (substrlen//2)

            i += 1

        return s[start:end+1]

    def max_substr_len(self, s, left, right):
        if not s or left > right:
            return 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right-left-1


myObj = Solution()
inpt = "bacabcbb"
print(myObj.longestPalindrome(inpt))
