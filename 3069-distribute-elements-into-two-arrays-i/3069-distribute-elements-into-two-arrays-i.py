class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        lst1 = [nums[0]]
        lst2 = [nums[1]]
        n = len(nums)
        for i in range(2,n):
            if lst1[-1]>lst2[-1]:
                lst1.append(nums[i])
            else:
                lst2.append(nums[i])
        return lst1+lst2