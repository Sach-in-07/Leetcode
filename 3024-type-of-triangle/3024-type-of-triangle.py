class Solution:
    def triangleType(self, nums: List[int]) -> str:
        mp = {}
        for i in range(3):
            if nums[i] not in mp:
                mp[nums[i]]=1
            else:
                mp[nums[i]]+=1
        if(not (nums[0] + nums[1] > nums[2] and
                nums[0] + nums[2] > nums[1] and
                nums[1] + nums[2] > nums[0])):return 'none'
        if len(mp)==3:return 'scalene'
        elif len(mp)==2:return 'isosceles'
        return 'equilateral'