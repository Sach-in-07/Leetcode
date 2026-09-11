from collections import Counter

class Solution:
    def totalNumbers(self, digits):
        cnt = Counter(digits)
        ans = 0
        for last in [0, 2, 4, 6, 8]:
            if cnt[last] == 0:
                continue
            cnt[last] -= 1
            
            for first in range(1, 10):
                if cnt[first] == 0:
                    continue

                cnt[first] -= 1

                ans += sum(1 for d in range(10) if cnt[d] > 0)

                cnt[first] += 1

            cnt[last] += 1

        return ans