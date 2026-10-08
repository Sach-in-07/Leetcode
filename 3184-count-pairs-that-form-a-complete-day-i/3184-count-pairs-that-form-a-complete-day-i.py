class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        freq = [0] * 24
        result = 0
        for h in hours:
            r = h % 24
            complement = (24 - r) % 24
            result += freq[complement]
            freq[r] += 1
        return result