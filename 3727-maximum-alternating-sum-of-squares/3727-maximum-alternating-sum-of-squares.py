class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        nums.sort()

        ans = 0
        n = len(nums)

        for i in range(n):
            if i < n // 2:
                ans -= nums[i] * nums[i]
            else:
                ans += nums[i] * nums[i]

        return ans