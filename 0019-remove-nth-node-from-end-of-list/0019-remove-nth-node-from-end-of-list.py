# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None:
            return None
        temp1 = head
        temp2 = head
        for _ in range(n):
            temp2 = temp2.next
        if temp2 is None:
            return head.next
        while temp2.next is not None:
            temp1 = temp1.next
            temp2 = temp2.next
        temp1.next = temp1.next.next

        return head