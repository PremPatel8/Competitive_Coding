from collections import defaultdict


class Solution:
    def solve(self, nums):
        res = num_len = len(nums)

        if num_len == 1:
            return res

        numdict = defaultdict(list)

        for itr, no in enumerate(nums):
            numdict[no].append(itr)

        for key in numdict:
            index_num = len(numdict[key])
            if index_num > 1:
                res += (((index_num-1) * index_num) // 2)

        return res

        # nums = [3, 1, 3, 0, 3, 3] = 3+2+1 = 6 = (3 * 4)/2
        # [3, 1, 0, 3, 3] 2+1 = 3 = 2 * (2+1) // 2
        # [0, 3, 3] = 2


myobj = Solution()
nums = [0, 3, 3]
print(myobj.solve(nums))
