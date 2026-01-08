from typing import List

"""
Problem Name: Maximum Subarray

Problem URL: https://leetcode.com/problems/maximum-subarray/

Problem Difficulty: Easy

Problem Section: Dynamic Programming

Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Resources:

"""
""" 202 / 202 test cases passed.
	Status: Accepted
Runtime: 68 ms
Memory Usage: 14.6 MB """

# Optimum Solution Greedy Dynamic Programming and Kadane's Algo:

# the max subarray sum at index i is either the max_sum for subarray ending at [i-1] + nums[i] or nums[i]
# (either we extend the prev subarry by adding nums[i] or start a new subarray from index i)
# find the max_price till index i, by using DP to keep track of max_price at each index i-1
# We can use a DP array (Linear Space) to store the max_price of subarray till each index i
# Then we can use the following formula to calculate min price at i:
# local_maximum[i] = max(A[i]+local_maximum[i-1], A[i])
# We can also convert it to (constant space) DP by storing the last curr sum in the curr_sum variable, as we only need the sum value till the last index
# update max_sum if it's less than curr_sum at price i


"""
Optimum Solution Greedy Dynamic Programming and Kadane's Algo:

Time complexity: O(N), where N is the length of nums.

We iterate through every element of nums exactly once.

Space complexity: O(1)

No matter how long the input is, we are only ever using 2 variables: currentSubarray and maxSubarray.

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize our variables using the first element.
        curr_sum = max_sum = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
    
    """
    Alt Divide and Conquer approach
    - Time complexity: O(N⋅logN), where N is the length of nums.
    On our first call to findBestSubarray, we use for loops to visit every element of nums. 
    Then, we split the array in half and call findBestSubarray with each half. 
    Both those calls will then iterate through every element in that half, 
    which combined is every element of nums again. Then, both those halves will be split in half, 
    and 4 more calls to findBestSubarray will happen, each with a quarter of nums.
    As you can see, every time the array is split, we still need to handle every element of the original input nums. 
    We have to do this logN times since that's how many times an array can be split in half.
    
    - Space complexity: O(logN), where N is the length of nums.
    The extra space we use relative to input size is solely occupied by the recursion stack. 
    Each time the array gets split in half, another call of findBestSubarray will be added to the recursion stack, 
    until calls start to get resolved by the base case - remember, the base case happens at an empty array, which occurs after logN calls.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)

        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)


myobj = Solution()
inpt = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(myobj.maxSubArray(inpt))
