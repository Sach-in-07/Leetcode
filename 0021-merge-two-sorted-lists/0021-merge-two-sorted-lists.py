# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        ans = dummy
        h1 = list1
        h2 = list2
        while h1 is not None and h2 is not None:
            if h1.val <= h2.val:
                ans.next = ListNode(h1.val)
                h1 = h1.next
            else:
                ans.next = ListNode(h2.val)
                h2 = h2.next
            ans = ans.next
        while h1!=None:
            ans.next = ListNode(h1.val)
            ans = ans.next
            h1 = h1.next
        while h2!=None:
            ans.next = ListNode(h2.val)
            ans = ans.next
            h2 = h2.next
        return dummy.next