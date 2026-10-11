# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1 = headA
        h2 = headB
        if h1 is  None or h2 is  None:
            return None

        cnt = 0
        while h1!=h2:
            h1 = h1.next
            h2 = h2.next
            if h1 == h2 : return h1
            if h1==None:
                h1 = headB
                cnt+=1
            if h2 == None:
                h2 = headA
                cnt+=1
        return h1
        