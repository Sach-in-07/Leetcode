class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        s = k
        while s:
            if mp.get(s,0) == 0:
                return s
            s+=k
        