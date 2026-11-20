# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split into two lists
        # find the middle node
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow is the end of the first list
        l1 = head
        l2 = slow.next
        slow.next = None # disconnect l1
        
        # reverse l2
        pre = None
        cur = l2
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        l2 = pre
        # merge l1 and reversed l2
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2


