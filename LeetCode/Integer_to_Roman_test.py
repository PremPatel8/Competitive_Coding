import Integer_to_Roman


def test_val3():
    assert Integer_to_Roman.Solution().intToRoman(3) == "III"


def test_val4():
    assert Integer_to_Roman.Solution().intToRoman(4) == "IV"


def test_val9():
    assert Integer_to_Roman.Solution().intToRoman(9) == "IX"


def test_val58():
    assert Integer_to_Roman.Solution().intToRoman(58) == "LVIII"


def test_val1994():
    assert Integer_to_Roman.Solution().intToRoman(1994) == "MCMXCIV"
