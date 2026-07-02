# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        s, f = head, head 
        while f.next is not None and f.next.next is not None:
            s = s.next
            f = f.next.next
        
        # reverse the second half and split
        second = s.next
        s.next = None
        prev = None
        while second is not None:
            temp = second.next
            second.next = prev  
            prev = second 
            second = temp
        second = prev
        # merge these 2 linked list together:


        dummy = ListNode()
        tail = dummy
        tail.next = head
        tail = tail.next
        while second is not None:
            t = second.next
            after = tail.next
            tail.next = second
            second.next = after
            tail = after
            second = t




   

