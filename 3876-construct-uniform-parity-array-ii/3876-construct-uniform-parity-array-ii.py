class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_even = 10**18
        min_odd = 10**18
        
        for i in range(len(nums1)):
            if nums1[i] % 2 == 0:
                if nums1[i] < min_even:
                    min_even = nums1[i]
            else:
                if nums1[i] < min_odd:
                    min_odd = nums1[i]
        
        if min_odd == 10**18:
            return True
        
        if min_even == 10**18:
            return True
        
        if min_odd < min_even:
            return True
        
        return False