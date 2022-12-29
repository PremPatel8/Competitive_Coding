from typing import List


class Solution:
    # Sol creating new result array
    #     def runningSum(self, nums: List[int]) -> List[int]:
    #         res = [nums[0]]

    #         for idx, no in enumerate(nums[1:],1):
    #             res.append(no+res[idx-1])

    #         return res

    # Sol reusing the input nums array
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx, no in enumerate(nums[1:], 1):
            nums[idx] = no + nums[idx-1]

        return nums
