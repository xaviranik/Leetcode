# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        a = 0
        b = len(height) - 1
        max_area = 0
        
        while a < b:
            if height[a] < height[b]:
                max_area = max(max_area, height[a] * (b-a))
                a += 1
            else:
                max_area = max(max_area, height[b] * (b-a))
                b -= 1
        return max_area