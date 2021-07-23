from typing import List

"""
Problem Name: Number of Non-Overlapping Sublists With Sum of Target

Problem URL: https://binarysearch.com/problems/Number-of-Non-Overlapping-Sublists-With-Sum-of-Target

Problem Section: 

Problem Statement:

Intuition

Hashset solution

We keep tracking the accumulated sums and store them in a hashset when we iterate the array. We can check if the value of current sum subtracting target exists in our hashset or not.
Implementation

One important thing, since we need to make sure these sublists are not overlapped, we have to forget all the previous sums if we can use the current sum to make a qualified sublist.
Time Complexity

We find all sublists with sum target with prefix sums. Let's say we're at index i and we know the prefix sum of [0, i] is acc. Then the sublist [a, i] has sum target exactly when the prefix sum [0, a) is acc - target.

The sum of a sublist can be calculated quickly with prefix sums. E.g., sum of a sublist at range (b, e] is prefix[e] - prefix[b]. Keep track of the indexes of the prefix sums to assist finding the index of prefix[i] - target.

(b, e] interval notation meaning, 
A bracket - [ or ] - means that end of the range is inclusive -- it includes the element listed. 
A parenthesis - ( or ) - means that end is exclusive and doesn't contain the listed element. 
So for [first1, last1), the range starts with first1 (and includes it), but ends just before last1.
or (b, e] - start at b but don't include it, end at e but include it

O(n)\mathcal{O}(n)O(n) ‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎
Space Complexity

O(n)\mathcal{O}(n)O(n) ‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎‎



Resources:
https://binarysearch.com/problems/Number-of-Non-Overlapping-Sublists-With-Sum-of-Target/solutions/5476197
https://binarysearch.com/problems/Number-of-Non-Overlapping-Sublists-With-Sum-of-Target/solutions/3912684

runtime: 
Your code took 151 milliseconds — faster than 89.66% in Python
"""

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n)


class Solution:
    def solve(self, nums, target):
        res = 0
        currPrefixSum = 0
        seen = set([0]) # need to add 0 for the case where the nums[i] value is equal to the target value

        for no in nums:
            currPrefixSum += no

            # we are looking for sublists whose sum equals target, and a quick way to calculate the sum of a sublist of range (b,e] is
            # prefixSum[e] - prefixSum[b]
            # so if prefixSum[e] - prefixSum[b] = target then
            # prefixSum[b] = prefixSum[e] - target
            # if prefixSum[b] exists in our set that means we have found a sublist whose total equals target,
            priorPrefixSum = currPrefixSum-target

            if priorPrefixSum in seen:
                res += 1
                # we need to clear the set as we do not allow overlap between sublists
                seen.clear()

            seen.add(currPrefixSum)

        return res


myobj = Solution()
# nums = [4, 3, 7, 5, -3, 10]
# target = 7
# ans = 3

nums = [-1, 1, -1]
target = 0
# ans = 1
print(myobj.solve(nums, target))
