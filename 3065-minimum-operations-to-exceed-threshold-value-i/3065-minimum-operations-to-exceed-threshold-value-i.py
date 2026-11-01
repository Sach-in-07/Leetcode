class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        less = 0
        for i in nums:
            if i<k:
                less+=1
        return less