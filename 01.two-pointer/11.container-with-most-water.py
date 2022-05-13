# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            currentArea = (r - l) * min(height[r], height[l])
            area = max(area, currentArea)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return area