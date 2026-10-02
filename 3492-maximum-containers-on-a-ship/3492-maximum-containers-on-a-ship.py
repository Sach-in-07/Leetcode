class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        if maxWeight> n*n*w:
            return n*n
        return maxWeight//w