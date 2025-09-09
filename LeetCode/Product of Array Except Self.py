from typing import List

"""
Problem Name: Product of Array Except Self

Problem URL: https://leetcode.com/problems/product-of-array-except-self/

Problem Difficulty: Medium

Problem Section: Array and Strings

Problem Statement:
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


Resources:

"""

""" 18 / 18 test cases passed.
	Status: Accepted
Runtime: 124 ms
Memory Usage: 20.5 MB """

# Solution techniques are - Optimized Left and Right (Prefix and Suffix) product lists solution

# Time complexity : O(n) Space complexity : O(1)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0]*length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


# Solution techniques are - Left and Right product lists, AKA Prefix and Suffix product lists

# Time complexity : O(n) Space complexity : O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The left and right arrays as described in the algorithm
        L, R, answer = [0]*length, [0]*length, [0]*length

        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):

            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):

            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]

        return answer
    
    
    # Divide by zero solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res


myobj = Solution()
inpt = [1, 2, 3, 4]
print(myobj.productExceptSelf(inpt))
