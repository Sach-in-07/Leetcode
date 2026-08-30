class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        last_idx = {}
        not_special = set()
        
        for i, x in enumerate(nums):
            if x in last_idx:
                if (i - last_idx[x]) > 1:
                    not_special.add(x)
            last_idx[x] = i
            
        return len(last_idx) - len(not_special)