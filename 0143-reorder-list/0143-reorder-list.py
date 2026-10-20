# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return

        def detectLoop(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        mid = detectLoop(head)

        h2 = mid.next
        mid.next = None
        h1 = reverse(h2)

        first = head

        while h1:
            first_next = first.next
            h1_next = h1.next

            first.next = h1
            h1.next = first_next

            first = first_next
            h1 = h1_next
        return head