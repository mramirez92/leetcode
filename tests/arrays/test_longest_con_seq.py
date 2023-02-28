from arrays.longest_con_seq import longest_consecutive
import pytest


def test_small_sequence():
    test = [1, 2, 3, 5, 6]
    assert longest_consecutive(test) == 3


def test_same_length():
    test = [1, 2, 7, 8]
    assert longest_consecutive(test) == 2


# @pytest.mark.skip
def test_list_with_gaps():
    test = [52, 100, 50, 6, 7, 51, 200]
    assert longest_consecutive(test) == 3


# edge cases: single, repeats, and empty list
def test_single():
    test = [1, 1, 1]
    assert longest_consecutive(test) == 1


# @pytest.mark.skip
def test_repeats():
    test = [2, 4, 2, 5, 1, 1, 4, 3, 6]
    assert longest_consecutive(test) == 6


# @pytest.mark.skip
def test_empty_list():
    test = []
    assert longest_consecutive(test) == 0
