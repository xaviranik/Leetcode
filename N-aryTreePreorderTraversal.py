# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Solution:
    def __init__(self):
        self.output = []

    def preorder(self, root):
        if root:
            self.output.append(root.val)
            if root.children:
                for child in root.children:
                    self.preorder(child)
        return self.output