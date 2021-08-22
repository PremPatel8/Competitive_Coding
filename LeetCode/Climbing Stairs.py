from typing import List

"""
Problem Name: Climbing Stairs

Problem Section: Dynamic Programming

Problem Statement:
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45

Resources:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/discuss/25296/3-4-short-lines-in-every-language
"""
""" 45 / 45 test cases passed.
	Status: Accepted
Runtime: 28 ms
Memory Usage: 14 MB """

# Solution techniques are Recursion with memoization, Dynamic Programming,
# Time complexity : O(n) Space complexity : O(n) DP solution (Bottom Up DP, iterative approach)
""" Complexity Analysis
Time complexity : O(n) Single loop upto n
Space complexity : O(n) dpdpdp array of size n is used.  """


class Solution:
    # Linear Space DP
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if not n:
            return 0

        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    # Constant Space DP
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if not n:
            return 0

        first = 1
        second = 2

        for _ in range(3, n+1):
            first, second = second, first+second

        return second


myobj = Solution()
n = 6
print(myobj.climbStairs(n))


# Recursion with Memoization (Top Down DP, recursive approach)
""" 
public class Solution {
    public int climbStairs(int n) {
        int memo[] = new int[n + 1];
        return climb_Stairs(0, n, memo);
    }
    public int climb_Stairs(int i, int n, int memo[]) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);
        return memo[i];
    }
}

Complexity Analysis
Time complexity : O(n)O(n)O(n). Size of recursion tree can go upto nnn.
Space complexity : O(n)O(n)O(n). The depth of recursion tree can go upto nnn. 
"""


# Fibonacci Number
""" 
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int first = 1;
        int second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }
}

Complexity Analysis
Time complexity : O(n)O(n)O(n). Single loop upto nnn is required to calculate nthn^{th}nth fibonacci number.
Space complexity : O(1)O(1)O(1). Constant space is used. 
 """

""" 
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
 """
