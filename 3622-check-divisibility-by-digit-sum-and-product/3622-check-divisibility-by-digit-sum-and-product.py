class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n<=9:return False
        d = n
        mul = 1
        add = 0
        while d>0:
            mul*= d%10
            add+=d%10
            d//=10
             
        return n%(mul+add) == 0