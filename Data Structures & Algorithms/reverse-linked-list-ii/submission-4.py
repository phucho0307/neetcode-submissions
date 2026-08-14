# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev1 = dummy
        oldHead = None
        prev = None
        
        for i in range (right):
            if i<left-2:
                head = head.next
            elif i == left-2:
                prev1 = head
                head = head.next
            elif i >= left-1:
                if i == left-1: oldHead = head
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
        oldHead.next = head
        prev1.next = prev
        return dummy.next            
