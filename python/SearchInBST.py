# https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution:
    def searchBST(self, root, val):
        if root is None:
            return
        if root.val == val:
            return root
        
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)