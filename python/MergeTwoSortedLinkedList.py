# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, l1, l2):
        temp = curr = ListNode(0)
        
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
            else:
                if l1:
                    curr.next = l1
                    l1 = l1.next
                if l2:
                    curr.next = l2 
                    l2 = l2.next
            curr = curr.next
                    
        return temp.next