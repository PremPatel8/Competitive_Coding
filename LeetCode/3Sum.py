from typing import List
import collections

"""
Problem Name: 15. 3Sum

Problem URL: https://leetcode.com/problems/3sum/

Problem Section: Array, 2 pointers

Problem Statement:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Resources:

runtime: 

"""

# Solution techniques are

# Time complexity : O() Space complexity : O()


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

class Solution:
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

    # Two pointer approach LeetCode
    # To make sure the result contains unique triplets, we need to skip duplicate values. 
    # It is easy to do because repeating values are next to each other in a sorted array.
    # After sorting the array, we move our pivot element nums[i] and analyze elements to its right. 
    # We find all pairs whose sum is equal -nums[i] using the two pointers pattern, 
    # so that the sum of the pivot element (nums[i]) and the pair (-nums[i]) is equal to zero.

    """ 318 / 318 test cases passed.
            Status: Accepted
        Runtime: 692 ms
        Memory Usage: 17.5 MB """

    """ 
    Time Complexity: O(n**2). twoSum is O(n), and we call it n times.

    Sorting the array takes O(nlog⁡n), so overall complexity is O(nlog⁡n+n**2). This is asymptotically equivalent to O(n**2).

    Space Complexity: from O(log⁡n) to O(n), 
    depending on the implementation of the sorting algorithm. For the purpose of complexity analysis, we ignore the memory required for the output.
 """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
            if nums[i] > 0:
                break
            # if at the first index (0) or if current no not same as previous number, call twosum from current index
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


# Solution using Dict / Hash Map and Set

""" 318 / 318 test cases passed.
	Status: Accepted
Runtime: 352 ms
Memory Usage: 18.1 MB """
""" Dict and Set approach """


# class Solution:
# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     if len(nums) < 3:
#         return []

#     count = collections.Counter(nums)
#     ans = []

#     # [0, 0, 0]
#     if count[0] > 2:
#         ans.append([0, 0, 0])

#     # [x, x, -2x]
#     for key in count.keys():
#         if count[key] > 1 and count[-key*2] > 0 and key != 0:
#             ans.append([key, key, -2*key])

#     # [x, y, -x-y]
#     sorted_keys = list(count.keys())
#     sorted_keys.sort()
#     key_set = set(sorted_keys)

#     for i in range(len(sorted_keys)-1):
#         for j in range(i+1, len(sorted_keys)):
#             num = -sorted_keys[i]-sorted_keys[j]

#             if num <= sorted_keys[j]:
#                 break

#             if num in key_set:
#                 ans.append([sorted_keys[i], sorted_keys[j], num])

#     return ans

""" 318 / 318 test cases passed.
        Status: Accepted
    Runtime: 860 ms
    Memory Usage: 18.1 MB """

# No-Sort approach
# If you cannot modify the input array, and you want to avoid copying it due to memory constraints

# Explanation for res set:
# We can put a combination of three values into a hashset to avoid duplicates.
# Values in a combination should be ordered (e.g. ascending).
# Otherwise, we can have results with the same values in the different positions.

# # Few optimizations so that it works efficiently for repeated values:
# Use another hashset dups to skip duplicates in the outer loop.
# Without this optimization, the submission will time out for the test case with 3,000 zeroes. This case is handled naturally when the array is sorted.

# Instead of re-populating a set every time in the inner loop, we can use a dict and populate it once.
# Values in the dict will indicate whether we have encountered that element in the current iteration.
# When we process nums[j] in the inner loop, we set its dict value to i. This indicates that we can now use nums[j] as a complement for nums[i].

""" 
    Time Complexity: O(n**2) We have outer and inner loops, each going through n elements.

    Space Complexity: O(n) for the hashset/hashmap.

    For the purpose of complexity analysis, we ignore the memory required for the output. 
    However, in this approach we also store output in the hashset for deduplication. 
    In the worst case, there could be O(n**2) triplets in the output, like for this example: [-k, -k + 1, ..., -1, 0, 1, ... k - 1, k]. 
    Adding a new number to this sequence will produce n / 3 new triplets.
 """

# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     res, dups = set(), set()
#     seen = {}
#     for i, val1 in enumerate(nums):
#         if val1 not in dups:
#             dups.add(val1)
#             for j, val2 in enumerate(nums[i+1:]):
#                 complement = -val1 - val2
#                 if complement in seen and seen[complement] == i:
#                     # sorted tuples to avoid duplicate results with same values in different positions
#                     res.add(tuple(sorted((val1, val2, complement))))
#                 seen[val2] = i
#     return res

""" 318 / 318 test cases passed.
            Status: Accepted
        Runtime: 968 ms
        Memory Usage: 18.1 MB """

# Sorting + Set approach

""" 
    Time Complexity: O(n**2). twoSum is O(n), and we call it n times.

    Sorting the array takes O(nlog⁡n), so overall complexity is O(nlog⁡n+n**2). This is asymptotically equivalent to O(n**2).

    Space Complexity: O(n) for the hashset.
 """

# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     res = []
#     nums.sort()

#     for i in range(len(nums)):
#         # If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
#         if nums[i] > 0:
#             break
#         # if at the first index (0) ot if current no not same as previous number, call twosum from current index
#         if i == 0 or nums[i - 1] != nums[i]:
#             self.twoSum(nums, i, res)

#     return res

# def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
#     seen = set()
#     j = i + 1

#     while j < len(nums):
#         complement = -nums[i] - nums[j]
#         if complement in seen:
#             res.append([nums[i], nums[j], complement])

#             # Increment j while the next value is the same as before to avoid duplicates in the result.
#             while j + 1 < len(nums) and nums[j] == nums[j + 1]:
#                 j += 1

#         seen.add(nums[j])
#         j += 1


myobj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
op = [[-1, -1, 2], [-1, 0, 1]]
print(f"{myobj.threeSum(nums)}=={op} => {myobj.threeSum(nums)==op}")
