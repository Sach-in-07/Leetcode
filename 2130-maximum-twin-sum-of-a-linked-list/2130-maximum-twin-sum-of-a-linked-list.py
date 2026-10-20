# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def mid(head):
            fast = head.next
            slow = head
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
        
        h1 = mid(head)
        h3 = h1.next
        h1.next = None
        h2 = reverse(h3)
        ans = 0
        h1 = head
        while h1 :
            ans = max(ans,h1.val+h2.val)
            h1 = h1.next
            h2 = h2.next
        return ans