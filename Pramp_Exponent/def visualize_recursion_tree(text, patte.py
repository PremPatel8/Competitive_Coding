def visualize_recursion_tree(text, pattern):
    """
    Visualize how different paths reach the same (i, j) states.
    """
    visited_states = {}
    path_id = [0]
    
    def dp(i, j, path_desc, depth=0):
        state = (i, j)
        path_id[0] += 1
        current_path_id = path_id[0]
        
        indent = "  " * depth
        state_str = f"({i},{j}): text[{i}:]='{text[i:]}' pattern[{j}:]='{pattern[j:]}'"
        
        if state in visited_states:
            print(f"{indent}🔄 Path #{current_path_id} reaches {state_str}")
            print(f"{indent}   ⚠️  DUPLICATE! Already visited by path(s): {visited_states[state]}")
            visited_states[state].append((current_path_id, path_desc))
            return True  # Early exit - already computed
        else:
            print(f"{indent}✨ Path #{current_path_id} reaches {state_str} via {path_desc}")
            visited_states[state] = [(current_path_id, path_desc)]
        
        if j == len(pattern):
            return i == len(text)
        
        first_match = i < len(text) and (pattern[j] == text[i] or pattern[j] == '.')
        
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            print(f"{indent}   Branch: pattern has '*' at position {j+1}")
            print(f"{indent}   → Path A: Skip '{pattern[j]}*'")
            dp(i, j + 2, f"skip {pattern[j]}*", depth + 1)
            if first_match:
                print(f"{indent}   → Path B: Use '{pattern[j]}*'")
                dp(i + 1, j, f"consume via {pattern[j]}*", depth + 1)
        else:
            if first_match:
                dp(i + 1, j + 1, f"match {pattern[j]}", depth + 1)
        
        return True
    
    print(f"Input: text='{text}', pattern='{pattern}'")
    print("=" * 80)
    dp(0, 0, "start")
    print("=" * 80)
    
    # Count duplicates
    duplicates = {k: v for k, v in visited_states.items() if len(v) > 1}
    print(f"\n📊 Summary:")
    print(f"   Total unique states: {len(visited_states)}")
    print(f"   States visited multiple times: {len(duplicates)}")
    
    if duplicates:
        print(f"\n   🎯 Duplicate states (these benefit from memoization):")
        for state, paths in duplicates.items():
            print(f"\n      State {state} reached {len(paths)} times:")
            for path_num, desc in paths:
                print(f"        - Path #{path_num}: {desc}")
    else:
        print(f"\n   ℹ️  No duplicate states in this example!")
    
    return len(duplicates) > 0


def count_calls_comparison(text, pattern):
    """Count actual function calls with and without memoization."""
    # Without memoization
    calls_without = [0]
    def no_memo(i, j):
        calls_without[0] += 1
        if j == len(pattern):
            return i == len(text)
        first_match = i < len(text) and (pattern[j] == text[i] or pattern[j] == '.')
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            return no_memo(i, j + 2) or (first_match and no_memo(i + 1, j))
        else:
            return first_match and no_memo(i + 1, j + 1)
    
    no_memo(0, 0)
    
    # With memoization
    calls_with = [0]
    cache_hits = [0]
    memo = {}
    def with_memo(i, j):
        calls_with[0] += 1
        if (i, j) in memo:
            cache_hits[0] += 1
            return memo[(i, j)]
        if j == len(pattern):
            result = i == len(text)
        else:
            first_match = i < len(text) and (pattern[j] == text[i] or pattern[j] == '.')
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                result = with_memo(i, j + 2) or (first_match and with_memo(i + 1, j))
            else:
                result = first_match and with_memo(i + 1, j + 1)
        memo[(i, j)] = result
        return result
    
    with_memo(0, 0)
    
    return calls_without[0], calls_with[0], len(memo), cache_hits[0]


# Demonstrations
if __name__ == "__main__":
    print("TESTING DIFFERENT PATTERNS FOR DUPLICATE STATES")
    print("=" * 80)
    
    # Test cases - some have duplicates, some don't
    test_cases = [
        ("aab", "c*a*b", "Your example - let's verify"),
        ("aa", "a*a*", "Two consecutive *s"),
        ("aaa", "a*a*a*", "Three consecutive *s"),
        ("aaab", "a*a*a*b", "Multiple *s then literal"),
        ("ab", ".*c*", "Dot-star with optional chars"),
    ]
    
    for text, pattern, description in test_cases:
        print(f"\n{'='*80}")
        print(f"TEST: {description}")
        print(f"{'='*80}\n")
        has_duplicates = visualize_recursion_tree(text, pattern)
        print()
    
    print("\n" + "=" * 80)
    print("PERFORMANCE COMPARISON ACROSS EXAMPLES")
    print("=" * 80)
    
    for text, pattern, description in test_cases:
        without, with_m, unique, hits = count_calls_comparison(text, pattern)
        print(f"\n{description}")
        print(f"  text='{text}', pattern='{pattern}'")
        print(f"  Without memo: {without:3d} calls")
        print(f"  With memo:    {with_m:3d} calls (cache hits: {hits})")
        print(f"  Unique states: {unique}")
        if hits > 0:
            print(f"  ✅ Memoization helped! Avoided {hits} redundant computation(s)")
        else:
            print(f"  ℹ️  No cache hits - no overlapping subproblems in this case")
    
    print("\n" + "=" * 80)
    print("EXPLANATION:")
    print("=" * 80)
    print("""
You were RIGHT to question my example! Let me clarify:

NOT ALL patterns create overlapping subproblems. It depends on the structure.

When DO we get duplicates (overlapping subproblems)?
✅ Patterns like "a*a*" - multiple *s for the SAME character
✅ Patterns like ".*.*" - multiple wildcards
✅ Complex patterns where different skip/consume choices converge

When DON'T we get duplicates?
❌ Patterns like "c*a*b" where each * is for a DIFFERENT character
❌ Simple linear patterns
❌ Patterns where branching paths naturally diverge

The key: '*' can match 0, 1, 2, ... chars. When you have multiple '*' patterns
that can match overlapping portions of text, THAT'S when paths converge.

So memoization is a "safety measure" - it helps when needed, and when it's not
needed (no duplicates), it's just a small overhead of maintaining a hash map.
    """)