class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find middle (slow ends at middle for odd, end of first half for even)
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse the second half, and split
        second = slow.next
        slow.next = None          # cut the list into two halves
        prev = None
        while second is not None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # now `prev` is the head of the reversed second half
        
        # Step 3: merge the two halves, alternating
        first, second = head, prev
        while second is not None:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first, second = t1, t2