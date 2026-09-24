class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def dig_sum(n):
            sum = 0
            while n>0:
                sum+=n%10
                n//=10
            return sum
        for i in range(len(nums)):
            if dig_sum(nums[i])==i:
                return i
        return -1