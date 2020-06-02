from collections import defaultdict
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numDict = defaultdict(int)

        for itr, n in enumerate(nums):
            numDict[n] = itr

        numcopy = sorted(nums, reverse=True)

        pstn1 = numDict[numcopy[0]]
        pstn2 = numDict[numcopy[1]]

        return (nums[pstn1]-1)*(nums[pstn2]-1)


myclass = Solution()

print(myclass.maxProduct([3, 4, 5, 2]))
