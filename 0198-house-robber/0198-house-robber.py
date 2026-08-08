class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2,n+1):
            pk = nums[i-1]+dp[i-2]
            n_pk = dp[i-1]
            dp[i] = max(n_pk,pk)
        return dp[n]