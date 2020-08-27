from typing import List

"""
Problem Name: House Robber

Problem Section: Dynamic Programming

Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 400

Resources:

"""
""" 69 / 69 test cases passed.
	Status: Accepted
Runtime: 24 ms
Memory Usage: 13.8 MB """

# Solution techniques are Plain Recursive (top-down), Recursive + memo (top-down), Iterative + memo (bottom-up), Iterative + N variables (bottom-up)
# Time complexity : O(n) Space complexity : O(1) DP Iterative Bottom Up solution using 2 variables


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prev1 = 0
        prev2 = 0

        for num in nums:
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp

        return prev1


myobj = Solution()
inpt = [2, 7, 9, 3, 1]
print(myobj.rob(inpt))


# Step 2. Recursive (top-down)
""" Converting the recurrent relation from Step 1 shound't be very hard.

public int rob(int[] nums) {
    return rob(nums, nums.length - 1);
}
private int rob(int[] nums, int i) {
    if (i < 0) {
        return 0;
    }
    return Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
}

This algorithm will process the same i multiple times and it needs improvement. Time complexity: [to fill] """

# Step 3. Recursive + memo (top-down).

""" int[] memo;
public int rob(int[] nums) {
    memo = new int[nums.length + 1];
    Arrays.fill(memo, -1);
    return rob(nums, nums.length - 1);
}

private int rob(int[] nums, int i) {
    if (i < 0) {
        return 0;
    }
    if (memo[i] >= 0) {
        return memo[i];
    }
    int result = Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
    memo[i] = result;
    return result;
}

Much better, this should run in O(n) time. Space complexity is O(n) as well, because of the recursion stack, let's try to get rid of it. """

# Step 4. Iterative + memo (bottom-up)

""" public int rob(int[] nums) {
    if (nums.length == 0) return 0;
    int[] memo = new int[nums.length + 1];
    memo[0] = 0;
    memo[1] = nums[0];
    for (int i = 1; i < nums.length; i++) {
        int val = nums[i];
        memo[i+1] = Math.max(memo[i], memo[i-1] + val);
    }
    return memo[nums.length];
} """

# Step 5. Iterative + 2 variables (bottom-up)
""" We can notice that in the previous step we use only memo[i] and memo[i-1], so going just 2 steps back. We can hold them in 2 variables instead. This optimization is met in Fibonacci sequence creation and some other problems [to paste links].

/* the order is: prev2, prev1, num  */
public int rob(int[] nums) {
    if (nums.length == 0) return 0;
    int prev1 = 0;
    int prev2 = 0;
    for (int num : nums) {
        int tmp = prev1;
        prev1 = Math.max(prev2 + num, prev1);
        prev2 = tmp;
    }
    return prev1;
} """
