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

# Time complexity : O() Space complexity : O()


class Solution:
    def solve(self, nums, target):
        res = 0
        prefixSum = 0
        seen = set([0])

        for no in nums:
            prefixSum += no

            if (prefixSum-target) in seen:
                res += 1
                seen.clear()

            seen.add(prefixSum)

        return res


myobj = Solution()
# nums = [4, 3, 7, 5, -3, 10]
# target = 7
# ans = 3

nums = [-1, 1, -1]
target = 0
# ans = 1
print(myobj.solve(nums, target))
