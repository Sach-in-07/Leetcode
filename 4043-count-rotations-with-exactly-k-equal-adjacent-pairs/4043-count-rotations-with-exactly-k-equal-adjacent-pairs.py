class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        cnt = 0
        
        for i in range(n):
            sb = s[i:] + s[:i]
            
            ans = self.rotate(sb, k)
            if ans == 1:
                cnt += 1
                
        return cnt

    def rotate(self, s: str, k: int) -> int:
        score = 0
        n = len(s)
        
        for i in range(n - 1, 0, -1):
            if s[i] == s[i - 1]:
                score += 1
                
        return 1 if score == k else 0