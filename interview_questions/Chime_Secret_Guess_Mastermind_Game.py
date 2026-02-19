from collections import Counter

""" Two Pass Hash Map / Counter Dict approach
⏱️ Time Complexity: O(N)

We can break this down by the operations performed:

    Sanitization: replace(" ", "") scans the string once → O(N).

    Pass 1 (Black Hits): We loop through the strings once to compare characters at the same index → O(N).

    Pass 2 (White Hits): * Creating the Counter (frequency map) for the remaining characters involves one pass over the remaining elements → O(N).

        Iterating over the unique keys in the dictionary to find the min() is at most O(N) (or O(K) where K is the number of unique colors).

    Total: O(N)+O(N)+O(N)=O(3N), which simplifies to O(N).

💾 Space Complexity: O(N)

The space used depends on how much "extra" information we store:

    Intermediate Lists: s_remaining and g_remaining can, in the worst case (where there are zero Black Hits), store all N characters → O(N).

    Frequency Maps: The Counter objects store unique characters as keys. In the worst case (every character is unique), this also scales with N → O(N).

    Total: O(N).
"""

def get_mastermind_score(secret, guess):
    # 1. Sanitize: Remove spaces and ensure they are same length
    s = secret.replace(" ", "")
    g = guess.replace(" ", "")
    
    if len(s) != len(g):
        return "Error: Secret and Guess must have the same number of colors."

    black_hits = 0
    white_hits = 0
    
    # We'll use these to store characters that weren't Black Hits
    s_remaining = []
    g_remaining = []

    # --- PASS 1: Identify Black Hits (Correct color, Correct position) ---
    for i in range(len(s)):
        if s[i] == g[i]:
            black_hits += 1
        else:
            # If it's not a Black Hit, save it for the White Hit check
            s_remaining.append(s[i])
            g_remaining.append(g[i])

    # --- PASS 2: Identify White Hits (Correct color, Incorrect position) ---
    # We use Counter to see how many of each color are left
    s_counts = Counter(s_remaining)
    g_counts = Counter(g_remaining)

    for color in g_counts:
        if color in s_counts:
            # The number of White Hits for a color is the minimum 
            # number of times it appears in both remaining sets.
            white_hits += min(s_counts[color], g_counts[color])

    return [black_hits, white_hits]

# --- Test Cases ---
# print(f"Unique Case: {get_mastermind_score('R G P O', 'R O G N')}") 
# Expected: [1, 2]

# print(f"Duplicate Case: {get_mastermind_score('R R P P', 'R Y R R')}") 
# Expected: [1, 1] (One 'R' is Black, only one more 'R' exists in secret for a White)
    
            

secret = "R G P O"
guess = "R O G N"
expected = [1,2]
result = get_mastermind_score(secret, guess)
print(f"result = {result} == expected = {expected} => {result==expected}")


secret = "R R G B"
guess = "R Y R R"
expected = [1,1]
result = get_mastermind_score(secret, guess)
print(f"result = {result} == expected = {expected} => {result==expected}")