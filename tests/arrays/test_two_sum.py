import pytest
from arrays.two_sum import two_sum


def test_target_sum():
    list_ = [3, 2, 4]
    expected = [1, 2]
    assert two_sum(list_, 6) == expected


def test_target_7():
    list_ = [1, 2, 3, 4, 5, 6]
    assert two_sum(list_, 7) == [2, 3]


def test_target_6():
    list_ =[3, 3]
    assert two_sum(list_, 6) == [0, 1]


def test_target_9():
    list_ =[2, 7, 11, 15]
    assert two_sum(list_, 9) == [0, 1]
