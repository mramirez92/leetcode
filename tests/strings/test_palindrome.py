from strings.palindrome import is_palindrome


def test_palindrome():
    s = "A man, a plan, a canal: Panama"
    assert is_palindrome(s) == True


def test_palindrome_racecar():
    s = "race a car"
    assert is_palindrome(s) == False


def test_palindrome_with_digits():
    s = "921129"
    assert is_palindrome(s) == True

def test_palindrome_alpha_digits():
    s = "Never 0dd 0r even"
    assert is_palindrome(s) == True
