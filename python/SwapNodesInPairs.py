# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        a = head
        b = head.next
        
        a.next = b.next
        b.next = a
        head = b
        
        a.next = self.swapPairs(a.next)
        return head