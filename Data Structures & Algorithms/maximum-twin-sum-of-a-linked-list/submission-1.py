# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head
        prev = slow
        res = 0
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        prev = None
        while slow is not None:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        while prev is not None:
            res = max(res, prev.val+ head.val)
            prev = prev.next
            head = head.next
        return res

        