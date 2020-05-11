# https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution:
    def findBottomLeftValue(self, root):
        self.ans = None
        self.max_level = -1
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, root, depth):
        if not root:
            return
        if depth > self.max_level:
            self.max_level = depth
            self.ans = root.val
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)