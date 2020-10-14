from typing import List
import collections

# Solution using 2 pointer
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         output = []
#         length = len(nums)

#         for xitr in range(length-2):
#             if nums[xitr] > 0:
#                 break

#             if xitr == 0 or xitr > 0 and nums[xitr] != nums[xitr-1]:
#                 lwrBnd = xitr+1
#                 uprBnd = length-1
#                 # ansSum = 0-x

#                 while lwrBnd < uprBnd:
#                     total = nums[xitr] + nums[lwrBnd] + nums[uprBnd]

#                     if total < 0:
#                         lwrBnd += 1
#                     elif total > 0:
#                         uprBnd -= 1
#                     elif total == 0:
#                         output.append([nums[xitr], nums[lwrBnd], nums[uprBnd]])

#                         while lwrBnd < uprBnd and nums[lwrBnd] == nums[lwrBnd+1]:
#                             lwrBnd += 1
#                         while lwrBnd < uprBnd and nums[uprBnd] == nums[uprBnd-1]:
#                             uprBnd -= 1

#                         lwrBnd += 1
#                         uprBnd -= 1

#         return output

# Solution using Dict / Hash Map / Set

""" 318 / 318 test cases passed.
	Status: Accepted
Runtime: 352 ms
Memory Usage: 18.1 MB """
""" Dict and Set approach """


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        count = collections.Counter(nums)
        ans = []

        # [0, 0, 0]
        if count[0] > 2:
            ans.append([0, 0, 0])

        # [x, x, -2x]
        for key in count.keys():
            if count[key] > 1 and count[-key*2] > 0 and key != 0:
                ans.append([key, key, -2*key])

        # [x, y, -x-y]
        sorted_keys = list(count.keys())
        sorted_keys.sort()
        key_set = set(sorted_keys)

        for i in range(len(sorted_keys)-1):
            for j in range(i+1, len(sorted_keys)):
                num = -sorted_keys[i]-sorted_keys[j]

                if num <= sorted_keys[j]:
                    break

                if num in key_set:
                    ans.append([sorted_keys[i], sorted_keys[j], num])

        return ans

    """ 318 / 318 test cases passed.
    Status: Accepted
    Runtime: 832 ms
    Memory Usage: 17.3 MB """
    """ Two pointer approach """

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums.sort()

    #     for i in range(len(nums)-2):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue

    #         left_idx, right_idx = i+1, len(nums)-1

    #         while left_idx < right_idx:
    #             s = nums[i] + nums[left_idx] + nums[right_idx]

    #             if s < 0:
    #                 left_idx += 1
    #             elif s > 0:
    #                 right_idx -= 1
    #             else:
    #                 res.append([nums[i], nums[left_idx], nums[right_idx]])
    #                 while left_idx < right_idx and nums[left_idx] == nums[left_idx+1]:
    #                     left_idx += 1
    #                 while left_idx < right_idx and nums[right_idx] == nums[right_idx-1]:
    #                     right_idx -= 1

    #                 left_idx += 1
    #                 right_idx -= 1

    #     return res


myobj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
op = [[-1, -1, 2], [-1, 0, 1]]
print(f"{myobj.threeSum(nums)}=={op} => {myobj.threeSum(nums)==op}")
