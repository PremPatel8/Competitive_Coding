from typing import List

"""
Problem Name: 39. Combination Sum

Problem URL: https://leetcode.com/problems/combination-sum/

Problem Section: 

Problem Statement:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.


Resources:

runtime: 
170 / 170 test cases passed.
	Status: Accepted
Runtime: 100 ms
Memory Usage: 14.2 MB
"""

# Solution techniques are Backtracking / DFS

# Time complexity : O() Space complexity : O()


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        self.backtrack(candidates, target, [], res)

        return res

    def backtrack(self, candidates, target, curr_combination, res):
        if target < 0:
            return

        if target == 0:
            res.append(curr_combination)
            return

        for i in range(len(candidates)):
            # we remove the ith candidate from available candidates when going down the path, because we want to avoid duplicate solutions, like 2,2,3 and 3,2,2
            self.backtrack(candidates[i:], target-candidates[i], curr_combination+[candidates[i]], res)


myobj = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(myobj.combinationSum(candidates, target))
