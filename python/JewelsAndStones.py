# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J, S):
        num_jewels = 0
        for char in S:
            if J.find(char) != -1:
                num_jewels += 1
        
        return num_jewels