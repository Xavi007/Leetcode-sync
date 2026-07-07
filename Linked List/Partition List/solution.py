class Solution:
    def partition(self, node: Optional[ListNode], pivot: int) -> Optional[ListNode]:

        left_dummy, right_dummy = ListNode(), ListNode()
        left_tail, right_tail = left_dummy, right_dummy

        curr = node

        while curr:
            if curr.val < pivot:
                left_tail.next = curr
                left_tail = left_tail.next
            else:
                right_tail.next = curr
                right_tail = right_tail.next

            curr = curr.next

        left_tail.next = right_dummy.next
        right_tail.next = None

        return left_dummy.next