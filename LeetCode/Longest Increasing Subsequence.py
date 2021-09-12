from typing import List

"""
Problem Name: Longest Increasing Subsequence

Problem URL: https://leetcode.com/problems/longest-increasing-subsequence/

Problem Difficulty: Medium

Problem Section: Dynamic Programming, Binary Search

Problem Statement:
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Resources:
https://leetcode.com/articles/longest-increasing-subsequence/#
Patience Sort
https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation

https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308

Solution Techniques:
Solution techniques are 
Dynamic Programming, 
search and replace to Intelligently Build a Subsequence, 
optimized search and replace using Binary Search
"""

# Approach 1: Dynamic Programming
""" Algorithm
Initialize an array dp with length nums.length and all elements equal to 1. 
dp[i] represents the length of the longest increasing subsequence that ends with the element at index i.

Iterate from i = 1 to i = nums.length - 1. At each iteration, use a second for loop to iterate from j = 0 to j = i - 1 (all the elements before i). 
For each element before i, check if that element is smaller than nums[i]. If so, set dp[i] = max(dp[i], dp[j] + 1).

Return the max value from dp.

Time Complexity - O(n^2)
Space Complexity - O(n)
 """

""" 54 / 54 test cases passed.
	Status: Accepted
Runtime: 3956 ms
Memory Usage: 14.6 MB """


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# Approach 2: Intelligently Build a Subsequence
"""
As stated in the previous approach, the difficult part of this problem is deciding if an element is worth using or not. Consider the example `nums = [8, 1, 6, 2, 3, 10]`. 
Let's try to build an increasing subsequence starting with an empty one: `sub = []`.

-   At the first element `8`, we might as well take it since it's better than nothing, so `sub = [8]`.
    
-   At the second element `1`, we can't increase the length of the subsequence since `8 >= 1`, so we have to choose only one element to keep. 
    Well, this is an easy decision, let's take the `1` since there may be elements later on that are greater than `1` but less than `8`, now we have `sub = [1]`.
    
-   At the third element `6`, we can build on our subsequence since `6 > 1`, now `sub = [1, 6]`.
    
-   At the fourth element `2`, we can't build on our subsequence since `6 >= 2`, but can we improve on it for the future? Well, similar to the decision we made at the second element, 
    if we replace the `6` with `2`, we will open the door to using elements that are greater than `2` but less than `6` in the future, so `sub = [1, 2]`.
    
-   At the fifth element `3`, we can build on our subsequence since `3 > 2`. Notice that this was only possible because of the swap we made in the previous step, 
    so `sub = [1, 2, 3]`.
    
-   At the last element `10`, we can build on our subsequence since `10 > 3`, giving a final subsequence `sub = [1, 2, 3, 10]`. The length of `sub` is our answer.
    

It appears the best way to build an increasing subsequence is: for each element `num`, if `num` is greater than the largest element in our subsequence, then add it to the subsequence. 
Otherwise, perform a linear scan through the subsequence starting from the smallest element and replace the first element that is greater than or equal to `num` with `num`. 
This opens the door for elements that are greater than `num` but less than the element replaced to be included in the sequence.

One thing to add: this algorithm does not always generate a valid subsequence of the input, 
but the length of the subsequence will always equal the length of the longest increasing subsequence. 
For example, with the input `[3, 4, 5, 1]`, at the end we will have `sub = [1, 4, 5]`, which isn't a subsequence, 
but the length is still correct. The length remains correct because the length only changes when a new element is larger than any element in the subsequence. 
In that case, the element is appended to the subsequence instead of replacing an existing element. """

""" 54 / 54 test cases passed.
	Status: Accepted
Runtime: 92 ms
Memory Usage: 14.6 MB """

""" 
Time complexity: O(N^2) only in the worst case

This algorithm will have a runtime of O(N^2) only in the worst case. Consider an input where the first half is [1, 2, 3, 4, ..., 99998, 99999], then the second half is [99998, 99998, 99998, ..., 99998, 99998]. We would need to iterate (N/2)^2 times for the second half because there are N/2N / 2N/2 elements equal to 99998, and a linear scan for each one takes N/2N / 2N/2 iterations. This gives a time complexity of O(N^2).

Despite having the same time complexity as the previous approach, in the best and average cases, it is much more efficient.

Space complexity: O(N)

When the input is strictly increasing, the sub array will be the same size as the input.
 """


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

                # Alt
                # for i in range(len(sub)):
                #     if sub[i] >= num:
                #         sub[i] = num
                #         break

        return len(sub)


# Approach 3: Improve With Binary Search, Best Time Complexity, Run time
"""
In the previous approach, when we have an element `num` that is not greater than all the elements in `sub`, 
we perform a linear scan to find the first element in `sub` that is greater than or equal to `num`. 
Since `sub` is in sorted order, we can use binary search instead to greatly improve the efficiency of our algorithm.

**Algorithm**

1.  Initialize an array `sub` which contains the first element of `nums`.
    
2.  Iterate through the input, starting from the second element. For each element `num`:
    -   If `num` is greater than any element in `sub`, then add `num` to `sub`.
    -   Otherwise, perform a binary search in `sub` to find the smallest element that is greater than or equal to `num`. Replace that element with `num`.
3.  Return the length of `sub`.
    

**Implementation**

In Python, the [bisect](https://docs.python.org/3/library/bisect.html) module provides super handy functions that does binary search for us. """

""" 54 / 54 test cases passed.
	Status: Accepted
Runtime: 64 ms
Memory Usage: 14.6 MB """

""" 
Time complexity: O(N⋅log⁡(N))

Binary search uses log⁡(N) time as opposed to the O(N) time of a linear scan, which improves our time complexity from O(N^2) to O(N⋅log⁡(N)).

Space complexity: O(N)

When the input is strictly increasing, the sub array will be the same size as the input.
 """


def lengthOfLIS(self, nums: List[int]) -> int:
    sub = []
    for num in nums:
        i = bisect_left(sub, num)

        # If num is greater than any element in sub
        if i == len(sub):
            sub.append(num)

        # Otherwise, replace the first element in sub greater than or equal to num
        else:
            sub[i] = num

    return len(sub)

# Personal implementation of bisect left algorithm using Binary Search


""" 54 / 54 test cases passed.
	Status: Accepted
Runtime: 88 ms
Memory Usage: 14.6 MB """


class Solution:
    # Find the index of the first element in sub that is greater than or equal to num
    def bisect_left_imp(self, sub, num):
        lo = 0
        # not len(sub)-1 because the num could need to be appened to the end of the list
        hi = len(sub)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if sub[mid] < num:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = self.bisect_left_imp(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)


myobj = Solution()
inpt = [10, 9, 2, 5, 3, 7, 101, 18]
# op = 4
print(myobj.lengthOfLIS(inpt))
