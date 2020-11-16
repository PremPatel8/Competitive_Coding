import Find_All_Anagrams_in_a_String


def test_findAnagrams():
    s = "cbaebabacd"
    p = "abc"

    assert Find_All_Anagrams_in_a_String.Solution().findAnagrams(s, p) == [0, 6]
