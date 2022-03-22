# https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return
        
        stack_node = []
        stack_sum = []
        
        stack_node.append(root)
        stack_sum.append(sum - root.val)
        
        while stack_node:
            current_node = stack_node.pop()
            current_sum = stack_sum.pop()
            
            if current_node.left is None and current_node.right is None and current_sum == 0:
                return True
            
            if current_node.left:
                stack_node.append(current_node.left)
                stack_sum.append(current_sum - current_node.left.val)
                
            if current_node.right:
                stack_node.append(current_node.right)
                stack_sum.append(current_sum - current_node.right.val)
        return False