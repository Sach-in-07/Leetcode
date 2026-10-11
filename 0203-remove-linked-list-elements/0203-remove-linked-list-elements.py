# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return head
        
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break
        

        h1 = head
        h2 = head
        while h1 is not None:
            if h1.val == val:
                h1 = h1.next
                h2.next = h1
            else:
                h2 = h1
                h1 =h1.next
        return head
                