from strings.anagrams import *


def test_anagram():
    str1 = "tar"
    str2 = "rat"
    assert is_anagram(str1, str2) is True


def test_anagram_false():
    str1 = "cart"
    str2 = "car"
    assert is_anagram(str1, str2) is False


def test_anagram_different_chars():
    str1 = "taco cat!"
    str2 = "cat! taco"
    str_num = "619-589-0033"
    str_num2 = "303-990-8517"
    assert is_anagram(str1, str2) is True
    assert is_anagram(str_num, str_num2) is False


def test_group_anagram():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagram(strs) == expected


def test_group_anagram_empty():
    strs = [""]
    assert group_anagram(strs) == [[""]]


def test_group_anagram_single():
    strs = ["a"]
    assert group_anagram(strs) == [["a"]]
