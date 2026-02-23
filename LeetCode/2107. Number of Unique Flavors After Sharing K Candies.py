from typing import List

"""
Problem Name: 2107. Number of Unique Flavors After Sharing K Candies

Problem URL: https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/description/

Problem Section: Sliding Window, Dict

Problem Difficulty: Medium

Problem Statement:
You are given a 0-indexed integer array candies, where candies[i] represents the flavor of the ith candy. Your mom wants you to share these candies with your little sister by giving her k consecutive candies, but you want to keep as many flavors of candies as possible.

Return the maximum number of unique flavors of candy you can keep after sharing with your sister.

 

Example 1:

Input: candies = [1,2,2,3,4,3], k = 3
Output: 3
Explanation: 
Give the candies in the range [1, 3] (inclusive) with flavors [2,2,3].
You can eat candies with flavors [1,4,3].
There are 3 unique flavors, so return 3.


Resources:

"""

"""
Solution technique: Sliding Window with Hash Map / Dict of candy flavor freq

Time & Space Complexity:
Here, N is the number of candies in the given array.

Time complexity: O(N)
We iterate through each candy only once, sliding the k-length window while counting the flavors fully contained within it. Since all operations on the map have amortized constant time complexity, the overall time complexity is O(N).

Space complexity: O(N)
The only additional space required is for the frequency map flavFreq, which stores the count of each of the N flavors. Therefore, the total space complexity is O(N).
"""

class Solution:
    def shareCandies(self, candies, k):
        # Store the total number of unique flavors in the array.
        flav_freq = defaultdict(int)
        for c in candies:
            flav_freq[c] += 1

        # Get the total number of unique flavors in the array.
        unique_flav = len(flav_freq)

        # Get the flavors used completely (freq is 0) in the window.
        used_in_window = 0
        for i in range(k):
            flav_freq[candies[i]] -= 1
            if flav_freq[candies[i]] == 0:
                used_in_window += 1

        # Get the flavors in the remaining array currently.
        max_flav = unique_flav - used_in_window

        # Slide the window to the right.
        for i in range(k, len(candies)):
            # Remove the candy on the left end from the window. 
            # Since it is no longer in the K len window of candies to be given,
            # we increment it's freq
            flav_freq[candies[i - k]] += 1
            
            # if the freq of this candy flavor increased from 0 to 1, then that means that it is no longer getting fully used in the current window
            if flav_freq[candies[i - k]] == 1:
                used_in_window -= 1

            # Add the candy on the right end at index i, into the K len window of candies to be given
            flav_freq[candies[i]] -= 1
            
            # if the freq of this candy flavor decreased from 1 to 0, then that means that it is fully getting used in the current window
            if flav_freq[candies[i]] == 0:
                used_in_window += 1

            max_flav = max(max_flav, unique_flav - used_in_window)

        return max_flav

"""
import file_name
def test_name():
    assert file_name.Solution().functionName(val) == OP
"""