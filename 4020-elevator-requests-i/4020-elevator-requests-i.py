class Solution:
    def elevatorRequests(self, n: int, nums: list[int]) -> int:
        sum = nums[0]
        for i in range(1,len(nums)):
            sum+= abs(nums[i-1]-nums[i])
        return sum