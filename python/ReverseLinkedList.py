# https://leetcode.com/problems/reverse-linked-list/

def reverse_list(self, head):
    prev_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node