# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        # remove head
        if length == n:
            return head.next
        
        # remove (length+1-n)th node
        count = 0
        pre = head
        while count < length-1-n:
            pre = pre.next
            count += 1
        pre.next = pre.next.next

        return head
        
