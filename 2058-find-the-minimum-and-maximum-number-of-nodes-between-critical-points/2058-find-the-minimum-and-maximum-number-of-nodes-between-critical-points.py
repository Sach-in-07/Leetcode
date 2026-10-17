# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        h1 = head
        h2 = head.next
        h3 = h2.next

        first = -1
        last = -1
        second_last = -1

        minm_dist = float('inf')
        maxm_dist = -1

        pos = 1

        while h3:
            if (h2.val > h1.val and h2.val > h3.val) or \
               (h2.val < h1.val and h2.val < h3.val):

                if first == -1:
                    first = pos
                else:
                    minm_dist = min(minm_dist, pos - last)
                    maxm_dist = pos - first

                second_last = last
                last = pos

            h1 = h2
            h2 = h3
            h3 = h3.next
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [minm_dist, maxm_dist]