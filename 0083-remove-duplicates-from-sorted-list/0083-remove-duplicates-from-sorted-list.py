# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        h1 = head
        h2 = head.next
        while h2 is not None:
            if h1.val == h2.val:
                h2 = h2.next
                h1.next = h2
            else:
                h1 = h2
                h2 = h2.next
        return head