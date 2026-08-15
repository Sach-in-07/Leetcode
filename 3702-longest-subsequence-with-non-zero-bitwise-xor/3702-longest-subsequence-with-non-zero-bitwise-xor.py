class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_all = 0
        n = len(nums)
        for i in range(n):
            xor_all ^=nums[i]
        if xor_all > 0:return n
        j = n-1
        
        while j>-1 and xor_all==0:
            xor_all^=nums[j]
            j-=1
        ans = j+1
        j=0
        while j<n and xor_all==0:
            xor_all^=nums[j]
            j+=1
        ans = max(ans,n-j-1)
        return ans