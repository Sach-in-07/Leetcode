class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        prf_sum = nums[0]
        cnt = 0
        if prf_sum == 0:
            cnt+=1
        n = len(nums)
        for i in range(1,n):
            prf_sum+=nums[i]
            if prf_sum == 0:
                cnt+=1
            
        return cnt