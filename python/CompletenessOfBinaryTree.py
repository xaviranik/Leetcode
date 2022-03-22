# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

class Solution:
    def isCompleteTree(self, root):
        queue = [root]
        no_children_allowed = False
        while queue:
            node = queue.pop(0)
            if node.left:
                if no_children_allowed:
                    return False
                else:
                    queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    else:
                        no_children_allowed = True
            elif node.right:
                # right child, no left child
                return False
            else: # no children
                no_children_allowed = True
        return True