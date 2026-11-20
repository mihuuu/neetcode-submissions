# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Better: one pass
        # two pointers (p2 is n steps away from p1)
        dummy = ListNode()
        dummy.next = head # first node might be deleted
        left = dummy
        right = head
        for _ in range(n):
            right = right.next
            
        while right:
            right = right.next
            left = left.next
        
        # remove left.next (left is the previous node)
        left.next = left.next.next

        return dummy.next