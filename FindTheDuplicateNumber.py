# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num