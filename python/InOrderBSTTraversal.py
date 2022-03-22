# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def in_orderTraversal(self, root):
        output = []

        def in_order_traverse(current):
            if current:
                in_order_traverse(current.left)
                output.append(current.val)
                in_order_traverse(current.right)
            return output

        if root is None:
            return []
        else:
            return in_order_traverse(root)