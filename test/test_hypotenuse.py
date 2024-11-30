import os

from hypotenuse.hypotenuse import hypotenuse


def test_secret():
    assert os.environ['SECRET'] == "It's gonna be legendary"


def test_hypotenuse():
    delta = 0.01

    assert hypotenuse(0, 0) == 0
    assert hypotenuse(0, 1) == 1
    assert hypotenuse(2, 0) == 4
    assert hypotenuse(4, 6) == 52
    assert hypotenuse(-1, 0) == 1
    assert hypotenuse(0, -3) == 9
    assert hypotenuse(-4, -1) == 17
    assert hypotenuse(-4, 5) == 41
    assert hypotenuse(2, -7) == 53
    assert abs(hypotenuse(2.5, 7.3) - 59.54) <= delta
