# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        h1 = head
        # cnt = k
        node_f = -1
        h3 = head
        while k>0:
            if k==1:
                node_f = h1.val
                h3 = h1
            k-=1
            h1=h1.next
        h2 = head
        while h1:
            h2 = h2.next
            h1 = h1.next
        node_s = h2.val
        h3.val = node_s
        h2.val = node_f
        return head
            