class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prd = 1
        while n>0:
            sum+= n%10
            prd*=n%10
            n//=10
        return prd-sum