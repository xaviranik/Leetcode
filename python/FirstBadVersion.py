# https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n):
        left = 0
        right = n
        
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            
        if left == right and isBadVersion(left):
            return left

        return -1