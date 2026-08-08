class Solution:
    def countValidPrefixes(self, s: str) -> int:
        res = 0
        diff = 0
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                diff+=1
            else:diff+=-1
            if abs(diff)<=1:res+=1
        return res        
        