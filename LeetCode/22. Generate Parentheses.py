from typing import List

"""
Problem Name: 22. Generate Parentheses

Problem Section: Backtracking

Problem Statement: 
Given `n` pairs of parentheses, write a function to _generate all combinations of well-formed parentheses_.

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

**Example 2:**

```
Input: n = 1
Output: ["()"]

```

**Constraints:**

-   `1 <= n <= 8`
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        This function will build valid combinations of parentheses of length 2n recursively.
        The function adds more parentheses to cur_string only when certain conditions are met:
        - If left_count < n, it suggests that a left parenthesis can still be added, so we add one left parenthesis to cur_string, creating a new string new_string = cur_string + (, and then call backtracking(new_string, left_count + 1, right_count).

        - If left_count > right_count, it suggests that a right parenthesis can be added to match a previous unmatched left parenthesis, so we add one right parenthesis to cur_string, creating a new string new_string = cur_string + ), and then call    backtracking(new_string, left_count, right_count + 1).

        - This function ensures that the generated string of length 2n is valid, and adds it directly to the answer. By only generating valid strings, we can avoid wasting time checking invalid strings.
    """
        def backtracking(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                result.append("".join(cur_string))
                return

            if left_count < n:
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                # To undo the change made to the shared list (cur_string) so that other recursive branches can use a clean state.
                cur_string.pop()

            if right_count < left_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                # To undo the change made to the shared list (cur_string) so that other recursive branches can use a clean state.
                cur_string.pop()

        result = []
        backtracking([], 0, 0)
        return result


myobj = Solution()

print(myobj.generateParenthesis(3))
