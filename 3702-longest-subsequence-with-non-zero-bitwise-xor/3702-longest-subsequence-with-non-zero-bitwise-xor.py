class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_all = 0
        has_nonzero = False
        n = len(nums)
        for i in range(n):
            xor_all ^=nums[i]
            if nums[i] != 0:
                has_nonzero = True
        if xor_all > 0:return n
        if has_nonzero:
            return n-1
        return 0