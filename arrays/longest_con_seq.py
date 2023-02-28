# longest consecutive sequence

def longest_consecutive(nums):
    num_set = set(nums)
    # current longest sequence
    longest = 0

    for num in nums:
        # if num has no previous, its the start of a sequence
        if (num - 1) not in num_set:
            length = 1
            while (num + length) in num_set:
                length += 1
            longest = max(length, longest)

    return longest

