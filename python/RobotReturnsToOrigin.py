# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for char in moves:
            if char == 'R':
                x += 1
            elif char == 'L':
                x -= 1
            elif char == 'U':
                y += 1
            elif char == 'D':
                y -= 1
        return x == 0 and y == 0