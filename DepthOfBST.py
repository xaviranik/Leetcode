# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        left = int(self.maxDepth(root.left))
        right = int(self.maxDepth(root.right))

        return max(left, right) + 1