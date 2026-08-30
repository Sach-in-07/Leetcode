class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        minm_idx = -1
        minm = 1000000
        maxm_idx = -1
        maxm = -1000000
        for i in range(n):
            if minm>nums[i]:
                minm = nums[i]
                minm_idx = i
            if maxm<nums[i]:
                maxm = nums[i]
                maxm_idx = i
        left = min(minm_idx, maxm_idx)
        right = max(minm_idx, maxm_idx)
        
        option_left = right + 1
        
        option_right = n - left
        
        option_mixed = (left + 1) + (n - right)
        
        return min(option_left, option_right, option_mixed)