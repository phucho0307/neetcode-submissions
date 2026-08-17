# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        cur = slow
        slow = slow.next
        cur.next = None
        prev = None
        while slow is not None:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        cur = head
        # merge 2 linked list together (head, prev)
        while head is not None and prev is not None:
            head = head.next
            cur.next = prev
            cur = prev
            prev = prev.next
            cur.next = head
            cur = head
        return 
