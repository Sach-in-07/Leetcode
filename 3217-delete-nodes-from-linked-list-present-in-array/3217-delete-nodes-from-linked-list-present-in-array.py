# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        if head is None:
            return
        h1 = head
        while mp.get(h1.val,0)>0:
            h1 = h1.next
        if h1 is None:
            return h1
        head = h1
        h2 = h1
        h2 = h2.next
        while h2:
            while h2 and mp.get(h2.val,0)>0:
                h2 = h2.next
            h1.next = h2
            if h2 is None:
                break
            h1 = h2
            h2 = h2.next
        return head