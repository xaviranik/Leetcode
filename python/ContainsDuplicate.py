# https://leetcode.com/problems/contains-duplicate/

def contains_duplicate(nums) -> bool:
    seen = set()
    for i, num in enumerate(nums):
        if num not in seen:
            seen.add(num)
        else:
            return True
    return False


print(contains_duplicate([1, 2, 5, 1]))
