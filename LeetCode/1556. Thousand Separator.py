class Solution:
    def thousandSeparator(self, n: int) -> str:
        str_num = str(n)
        str_num = str_num[::-1]

        res = '.'.join(str_num[i:i + 3] for i in range(0, len(str_num), 3))

        return res[::-1]


myobj = Solution()
inpt = 123456789
print(myobj.thousandSeparator(inpt))
