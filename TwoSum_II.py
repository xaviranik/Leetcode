# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def two_sum_sorted(numbers, target):
    comp = dict()
    for i, num in enumerate(numbers):
        if num not in comp:
            comp[target - num] = i + 1
        else:
            return [comp[num], i + 1]


def two_sum_sorted_alt(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1
    while p1 <= p2:
        s = numbers[p1] + numbers[p2]
        if s < target:
            p1 += 1
        elif s > target:
            p2 -= 1
        else:
            return [p1 + 1, p2 + 1]


print(two_sum_sorted([1, 4, 6, 10], 14))