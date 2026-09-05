class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def solve(st,n,k,curr):
            if k==0:
                ans.append(curr[:])
                return
            if st>n:
                return
            curr.append(st)
            solve(st+1,n,k-1,curr)
            curr.pop()
            solve(st+1,n,k,curr)
        solve(1,n,k,[])
        return ans