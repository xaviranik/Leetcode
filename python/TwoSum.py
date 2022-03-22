# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    comp = dict()

    for i, n in enumerate(nums):
        if n in comp:
            return [comp[n], i]
        comp[target - n] = i

a = [3, 2, 4, 1]
print(two_sum(a, 6))
