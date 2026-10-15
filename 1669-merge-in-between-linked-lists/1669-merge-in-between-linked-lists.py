# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h1 = list1
        for c in range(a - 1):
            h1 = h1.next
        h2 = h1
        for c in range(b - a + 2):
            h2 = h2.next
        h1.next = list2
        while list2.next!=None:
            list2 = list2.next
        list2.next = h2
        return list1