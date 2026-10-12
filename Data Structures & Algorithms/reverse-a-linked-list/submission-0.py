# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None          # nothing comes before the first node; it becomes the new tail
        curr = head
        while curr:          # loop until we've walked off the end (also handles empty list)
            nxt = curr.next  # 1. save the rest of the list before we break the link
            curr.next = prev # 2. rewire: point this node backwards
            prev = curr      # 3. move prev up to this node
            curr = nxt       # 4. move curr to the saved next node
        return prev          # curr is None now; prev is the old last node = new head
        
        

        