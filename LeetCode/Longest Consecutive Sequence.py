from typing import List

"""
Problem Name: Longest Consecutive Sequence

Problem Section: Array and Strings

Problem Statement:
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Resources:
"""
    
    
# Brute Force using Set
# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

# Sorting
# Time complexity : O(nlogn)
# Space complexity : O(logn) or O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
    

# Set
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_streak = 0

        for num in numSet:
            # We check for num-1 because, ensuring that the number that would immediately precede the current number in a sequence is not present, 
            # as that number would necessarily be part of a longer sequence.
            if (num - 1) not in numSet:
                current_streak = 1
                while (num + current_streak) in numSet:
                    current_streak += 1
                
                longest_streak = max(current_streak, longest_streak)
                
        return longest_streak



myobj = Solution()
inpt = [100, 4, 200, 1, 3, 2]
print(myobj.longestConsecutive(inpt))
