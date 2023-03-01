# 242. Valid Anagram

def is_anagram(str1, str2):
    return True if sorted(str1) == sorted(str2) else False


# 49. Group Anagram
def group_anagram(strs):
    groups = {}
    for item in strs:
        sorted_key = "".join(sorted(item))

        if sorted_key not in groups:
            groups[sorted_key] = []
        groups[sorted_key].append(item)
    return list(groups.values())
