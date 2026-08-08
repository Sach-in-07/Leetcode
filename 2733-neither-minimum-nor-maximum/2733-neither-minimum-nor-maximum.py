class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:return -1
        lst = [0]*(101)
        for i in nums:
            lst[i]+=1
        cnt = 0
        for i in range(101):
            if lst[i]>0:
                cnt+=1
            if cnt==2:return i
        