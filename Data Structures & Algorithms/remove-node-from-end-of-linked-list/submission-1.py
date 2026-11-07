# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size, tail = self.sizecheck(head)
        node = head
        print(size)
        targetnode = size + 1 - n #this is the node we wish to remove
        print (targetnode)
        ## set the next of the node before the target node to be the same as the target node (effectively removing the target node from the linked list)
        #beforetarget.next = beforetarget.next.next
        #return head
        #edge case is when target node is the last node in the list. This occurs when n = 1. Other edge case is when the targetnode is the head of the linked list
        if targetnode == 1:
            head = head.next
            return head
        else: 
            counter = 1 
            while counter != targetnode-1:
                counter += 1
                node = node.next 
            node.next = node.next.next
            return head
    



    
    def sizecheck(self, head):
        nextnode = 1 
        size = 0
        while nextnode != None:
            size +=1
            nextnode = head.next
            if head.next != None:
                head = head.next
        return size, head



