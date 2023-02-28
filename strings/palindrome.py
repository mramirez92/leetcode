def is_palindrome(str):
    clean = [i for i in str.lower() if i.isalnum()]
    if "".join(clean) == "".join(clean[::-1]):
        return True
    else:
        return False
