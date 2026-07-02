# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None: return None
        k = head
        g = head
        l=1
        while k.next is not None:
            l+=1
            k=k.next
        steps = l - n - 1 
        if n==l: return head.next
        for i in range (steps):
            g = g.next
        g.next = g.next.next
        return head




        