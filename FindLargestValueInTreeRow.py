# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution:
    def largestValues(self, root):
        res = []
        
        def dfs(node, depth):
            if not node:
                return
            
            if len(res) == depth:
                res.append(node.val)
            elif res[depth] < node.val:
                res[depth] = node.val
                
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res