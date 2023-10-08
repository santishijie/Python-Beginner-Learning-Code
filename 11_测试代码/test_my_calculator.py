from my_calculator import my_addr


def test_positive():
    assert my_addr(3, 9) == 12


def test_negative():
    assert my_addr(-3, 9) == 6
