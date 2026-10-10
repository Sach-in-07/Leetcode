# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        h1 = head.next
        h2 = head.next.next

        while h1 is not None and h2 is not None and h2.next is not None:
            if h1 == h2:
                return True
            h1 = h1.next
            h2 = h2.next.next

        return False