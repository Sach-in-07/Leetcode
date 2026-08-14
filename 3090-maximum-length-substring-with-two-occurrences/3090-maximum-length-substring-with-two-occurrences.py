class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mp = {}
        n = len(s)
        i = 0
        j = 0
        ans = 0
        k = 2
        while i < n and j < n:
            mp[s[j]] = mp.get(s[j], 0) + 1

            while mp[s[j]] > k:
                mp[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

            j += 1

        return ans