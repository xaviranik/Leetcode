# https://leetcode.com/problems/univalued-binary-tree/

class Solution:
    def isUnivalTree(self, root):
        right_univalued = root.right == None or root.right.val == root.val and self.isUnivalTree(root.right)
        left_univalued = root.left == None or root.left.val == root.val and self.isUnivalTree(root.left)
        
        return right_univalued and left_univalued