# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        
        h1 = head
        h2 = head.next
        while h2.next is not None and h2.next.next is not None:
            h1 = h1.next
            h2 = h2.next.next
        return h1.next