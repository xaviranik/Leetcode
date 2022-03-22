# https://leetcode.com/problems/odd-even-linked-list/

class Solution:
    def oddEvenList(self, head):
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        odd.next = even_head
        
        return head