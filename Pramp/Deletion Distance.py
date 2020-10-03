"""
Deletion Distance

The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:
By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.

Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

STR1 = HEAT
STR2 = HIT
ANS - 3

   '' H E A T
''  0 1 2 3 4
H   1 0 1 2 3
I   2 1 2 3 4
T   3 2 3 4 3

base case:
empty string - don't delete - 0

if chars match:
dp[i][j] = dp[i-1][j-1]

if chars mismatch:
dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
"""


def deletion_distance(str1, str2):
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

    for i in range(len(str1)+1):
        dp[i][0] = i

    for j in range(len(str2)+1):
        dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if (str1[i-1] == str2[j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1

    return dp[len(str1)][len(str2)]


str1 = "hit"
str2 = "heat"

# str1 = ""
# str2 = ""
print(deletion_distance(str1, str2))
