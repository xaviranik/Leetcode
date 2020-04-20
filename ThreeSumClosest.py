# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        
        for i in range(0, len(nums) - 2):
            a = i + 1
            b = len(nums) - 1
            
            while a < b:
                current_sum = nums[a] + nums[b] + nums[i]
                if current_sum > target:
                    b -= 1
                else:
                    a += 1
                
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum
        return result