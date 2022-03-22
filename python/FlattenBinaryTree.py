# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        q = []
        def helper(node):
            if not node:
                return
            q.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
                
        helper(root)
        if q:
            q.pop(0)
        
            while q:
                if root:
                    root.left = None
                    root.right = TreeNode(q.pop(0))
                    root = root.right