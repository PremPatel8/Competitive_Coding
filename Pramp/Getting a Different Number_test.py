import importlib
foobar = importlib.import_module("Getting a Different Number")


def test_get_different_number():
    assert foobar.get_different_number([0, 1, 2, 3]) == 4


def test_get_different_number_1():
    assert foobar.get_different_number([0, 99999, 100000]) == 1


def test_get_different_number_2():
    assert foobar.get_different_number([0]) == 1


def test_get_different_number_3():
    assert foobar.get_different_number([0, 1, 2]) == 3


def test_get_different_number_4():
    assert foobar.get_different_number([1, 3, 0, 2]) == 4


def test_get_different_number_5():
    assert foobar.get_different_number([100000]) == 0


def test_get_different_number_6():
    assert foobar.get_different_number([1, 0, 3, 4, 5]) == 2


def test_get_different_number_7():
    assert foobar.get_different_number([0, 100000]) == 1


def test_get_different_number_8():
    assert foobar.get_different_number([0, 5, 4, 1, 3, 6, 2]) == 7
