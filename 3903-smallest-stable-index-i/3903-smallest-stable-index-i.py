class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [0]*n
        suffix[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = min(suffix[i+1],nums[i])
        # print(suffix)
        maxm = -1
        ans = -1
        for i in range(n):
            maxm = max(nums[i],maxm)
            val = maxm - suffix[i]
            if val<=k:
                ans = i
                break 
        return ans
