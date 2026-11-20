# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # new list
        head = ListNode() # dummy node pointing to the result list
        cur = head
        
        l1 = list1
        l2 = list2
        while l1 and l2:
            # compare val from both lists
            # use the smaller node
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        # add the remaining nodes
        if l1:
            cur.next = l1
        
        if l2:
            cur.next = l2
        
        return head.next
            