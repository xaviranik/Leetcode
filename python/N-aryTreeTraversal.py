# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

def post_order_traversal(root):
    output = []
    if root is None:
        return output

    def post_order(root):
        if root is None:
            return

        for child in root.children:
            post_order(child)
            output.append(child.val)

    post_order(root)
    output.append(root.val)

    return output
