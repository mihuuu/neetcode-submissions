# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Better: one pass
        # two pointers (p2 is n steps away from p1)
        p1 = head
        count = 0
        while count < n:
            p1 = p1.next
            count += 1
        
        if not p1:
            return head.next
            
        p2 = head
        while p1.next:
            p2 = p2.next
            p1 = p1.next
        
        p2.next = p2.next.next

        return head