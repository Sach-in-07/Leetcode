class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mp = {}
        n = len(nums)
        i = 0
        j = 0
        ans = -1
        while i < n and j < n:
            if nums[j] not in mp:
                mp[nums[j]] = 1
            else:
                mp[nums[j]] += 1

            if mp[nums[j]] > k:
                while mp[nums[j]] > k and i < j:
                    mp[nums[i]] -= 1
                    i += 1

                ans = max(ans, j - i + 1)
            else:ans = max(ans, j - i + 1)
            j+=1
        return ans