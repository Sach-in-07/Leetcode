# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None or head.next is None:
            return True
        sl = head
        ft = head
        while ft is not None and ft.next is not None:
            sl = sl.next
            ft = ft.next.next
        if ft is not None:
            sl = sl.next
        
        prv = None
        curr = sl

        while curr is not None:
            nxt  = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
        r_head = prv
        h1 = head
        h2  = r_head
        result = True

        while h2 is not None:
            if h1.val != h2.val:
                result = False
                break
            h1 = h1.next
            h2 = h2.next
        return result