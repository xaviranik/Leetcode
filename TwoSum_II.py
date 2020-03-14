# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def two_sum_sorted(numbers, target):
    comp = dict()
    for i, num in enumerate(numbers):
        if num not in comp:
            comp[target - num] = i + 1
        else:
            return [comp[num], i + 1]


print(two_sum_sorted([1, 4, 6, 10], 14))