
""" Memoization Solution """
def is_match(text: str, pattern: str) -> bool:
    memo = {}
    
    def isMatch_helper(txt_idx, pat_idx):
        if (txt_idx, pat_idx) in memo:
            return memo[(txt_idx, pat_idx)]
        
        # If pattern is exhausted, text must also be exhausted
        if pat_idx == len(pattern):
            return txt_idx == len(text)
        
        # Check if current characters match
        first_match = txt_idx < len(text) and (pattern[pat_idx] == text[txt_idx] or pattern[pat_idx] == '.')
        
        # Handle '*' if it's the next character
        if pat_idx + 1 < len(pattern) and pattern[pat_idx + 1] == '*':
            # Two options:
            # 1. Skip the 'char*' pattern (match zero occurrences)
            # 2. If first char matches, consume it and keep the pattern (match one or more)
            result = isMatch_helper(txt_idx, pat_idx + 2) or (first_match and isMatch_helper(txt_idx + 1, pat_idx))
        else:
            # No '*', so current characters must match
            result = first_match and isMatch_helper(txt_idx + 1, pat_idx + 1)
        
        memo[(txt_idx, pat_idx)] = result
        return result
    
    return isMatch_helper(0, 0)


""" 2D DP Solution 
Visual Example: text = "aa", pattern = "a*"
        01
text = "aa", 
            01
pattern =  "a*"

         0     1      2
        ""     a      a*
      ┌─────┬─────┬─────┐
 0 "" │  T  │  F  │  T  │  ← empty text matches "" and "a*" (zero a's)
      ├─────┼─────┼─────┤
 1 a  │  F  │  T  │  T  │  ← "a" matches "a" and "a*"
      ├─────┼─────┼─────┤
 2 aa │  F  │  F  │  T  │  ← "aa" only matches "a*"
      └─────┴─────┴─────┘

"""

def isMatch(text, pattern):
    # dp[i][j] = True if text[:i] matches pattern[:j]
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    
    # Empty text matches empty pattern
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, c*a* etc. that can match empty string by matching **zero occurrences** of each character.
    """ 
    - `j` is the column index (1-indexed in the dp table)
    - `pattern[j-1]` is the actual pattern character (0-indexed)
    - If we see a `*`, we can skip the `char*` pair by looking 2 columns back: `dp[0][j-2]`
    """
    for j in range(2, len(pattern) + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    # We iterate through each cell, starting from row 1, column 1 (skipping the base cases we already set).
    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == '*':
                # '*' matches zero occurrences of previous character
                dp[i][j] = dp[i][j - 2]
                
                # '*' matches one or more occurrences
                # Check if current text char matches the char before '*'
                if pattern[j - 2] == '.' or pattern[j - 2] == text[i - 1]:
                    # `dp[i-1][j]` means: "consume one character from text, keep the same pattern position (because `*` can match more)"
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                # Current characters must match (or pattern has '.')
                if pattern[j - 1] == '.' or pattern[j - 1] == text[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
    
    return dp[len(text)][len(pattern)]



""" Alternative: DP with space optimization (most efficient) """

def isMatch_optimized(text, pattern):
    """
    Space-optimized version using 1D DP array.
    Time: O(m*n), Space: O(n)
    """
    m, n = len(text), len(pattern)
    
    # Use only two rows instead of full 2D array
    prev = [False] * (n + 1)
    prev[0] = True
    
    # Initialize for patterns like a*, a*b*
    for j in range(2, n + 1):
        if pattern[j - 1] == '*':
            prev[j] = prev[j - 2]
    
    for i in range(1, m + 1):
        curr = [False] * (n + 1)
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                curr[j] = curr[j - 2]
                if pattern[j - 2] == '.' or pattern[j - 2] == text[i - 1]:
                    curr[j] = curr[j] or prev[j]
            else:
                if pattern[j - 1] == '.' or pattern[j - 1] == text[i - 1]:
                    curr[j] = prev[j - 1]
        prev = curr
    
    return prev[n]

  
# debug your code below
print(is_match("aa", "a"))

print(is_match("aa", "a*a*"))