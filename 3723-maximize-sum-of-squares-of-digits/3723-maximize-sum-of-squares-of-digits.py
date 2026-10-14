class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        ans = []

        while sum > 0:
            digit = min(9, sum)
            ans.append(str(digit))
            sum -= digit

        ans.extend(['0'] * (num - len(ans)))

        return ''.join(ans)