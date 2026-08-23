class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        lft_q = 0
        rt_q = 0
        lft_sum = 0
        rt_sum = 0
        for i in range(n):
            if num[i] == '?':
                if i < n//2:
                    lft_q+=1
                else:
                    rt_q+=1
            else:
                if i < n//2:
                    lft_sum+=int(num[i])
                else:
                    rt_sum+=int(num[i])
        if (lft_q+rt_q)%2==1:return True
        return ((2*lft_sum+9*lft_q)==(2*rt_sum+9*rt_q)) ==False