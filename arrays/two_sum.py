"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""


def two_sum(nums, target):
    checked = {}
    i = 0
    while target - nums[i] not in checked:
        checked[nums[i]] = i
        i += 1
    return [checked[target - nums[i]], i]


# 167. two sum array is sorted
def two_sum_sorted(numbers, target):
    checked = {}
    i = 0
    while target - numbers[i] not in checked:
        checked[numbers[i]] = i
        i += 1
    return [checked[target - numbers[i]] + 1, i + 1]
