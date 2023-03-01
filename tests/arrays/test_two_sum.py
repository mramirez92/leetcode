import pytest
from arrays.two_sum import two_sum, two_sum_sorted


def test_two_sum():
    list_ = [3, 2, 4]
    expected = [1, 2]
    assert two_sum(list_, 6) == expected


def test_two_sum_7():
    list_ = [1, 2, 3, 4, 5, 6]
    assert two_sum(list_, 7) == [2, 3]


def test_two_sum_6():
    list_ = [3, 3]
    assert two_sum(list_, 6) == [0, 1]


def test_two_sum_9():
    list_ = [2, 7, 11, 15]
    assert two_sum(list_, 9) == [0, 1]


def test_sum_sorted():
    numbers = [2, 7, 11, 15]
    nums = [2, 3, 4]
    assert two_sum_sorted(numbers, 9) == [1, 2]
    assert two_sum_sorted(nums, 6) == [1, 3]


def test_sum_sorted_negatives():
    first = [-1, 0]
    second = [-3, -2, 2, 4]
    assert two_sum_sorted(first, -1) == [1, 2]
    assert two_sum_sorted(second, 1) == [1, 4]
