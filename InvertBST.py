# https://leetcode.com/problems/invert-binary-tree/submissions/

class Solution:
    def invertTree(self, root):
        if root is None:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.right = left
        root.left = right

        return root