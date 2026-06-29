# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        else:
            l = 0
            k = head
            while k is not None:
                k = k.next
                l+=1
            g = None
            for i in range (l):
                prev = head.next
                head.next = g
                g = head
                head = prev
            return g


        