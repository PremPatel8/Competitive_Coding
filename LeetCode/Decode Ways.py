class Solution:
    def numDecodings(self, s:str) -> int:
        if len(s) == 0 or s is None:
            return 0

        # @lru_cache(maxsize=None)
        def dfs(string):
            # if len(string)>0:
            #     if string[0] == '0':
            #         return 0
            if string == "" or len(string) == 1:
                return 1
            if int(string[0:2]) <= 25:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first+second
            else:
                return dfs(string[1:])

        result_sum = dfs(s)

        return result_sum


myobj = Solution()
inpt = "100200300"
print(myobj.numDecodings(inpt))
