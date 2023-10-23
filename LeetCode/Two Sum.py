from typing import List
from collections import Counter
"""
Problem Name: Two Sum

Problem Section: Array

Problem Statement:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Resources:
"""
""" 29 / 29 test cases passed.
	Status: Accepted
Runtime: 44 ms
Memory Usage: 15.3 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(n) Optimized One-pass Hash Table / Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        if not nums or len(nums) == 0:
            return res

        if len(nums) == 2:
            if (nums[0]+nums[1]) == target:
                res = [0, 1]
            return res

        numIndex = dict()

        for i, no in enumerate(nums):
            complement = target-no

            if complement in numIndex:
                res = [numIndex[complement], i]
                break

            numIndex[no] = i

        return res
    
# My Python Dict solution with fewer lines of code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for idx, no in enumerate(nums):
            diff = target-no
            
            if diff in seen:
                return [seen[diff], idx]
            else:
                seen[no] = idx


# My Java HashMap solution
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] output = new int[2];
        Map<Integer, Integer> numIndex = new HashMap<Integer, Integer>();

        for(int idx=0; idx < nums.length; idx++) {
            int num = nums[idx];
            int complement = target-num;

            if(numIndex.containsKey(complement)) {
                output[0] = idx;
                output[1] = numIndex.get(complement);
                return output;
            } else {
                numIndex.put(num, idx);
            }
        }
        return output;
    }
}

myobj = Solution()
nums = [2, 7, 11, 15]
target = 9
print(myobj.twoSum(nums, target))
