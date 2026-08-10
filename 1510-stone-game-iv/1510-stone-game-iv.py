class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        lst = [-1]*(n+1)

        def solve(n):
            if n==0:
                return False
            if lst[n]!=-1:
                return lst[n]
            k = (int)(n**(1/2))
            for i in range(1,k+1):
                if solve(n-i*i) == False:
                    lst[n]=True
                    return lst[n] 
            lst[n]=False
            return lst[n]
        return solve(n)