class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = [i]
            else:
                mp[nums[i]].append(i)
        ans = 0
        for i in mp:
            if len(mp[i]) == 3 and (mp[i][1]-mp[i][0]) == (mp[i][2]-mp[i][1]):
                ans+=1
        return ans