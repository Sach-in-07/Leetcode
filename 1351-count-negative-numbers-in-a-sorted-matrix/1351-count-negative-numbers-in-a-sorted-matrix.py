class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        ans = 0
        # for i in grid:
        #     for j in i:
        #         if j <0:
        #             ans+=1
        # return ans

        for i in range(len(grid)):
            for j in range(-1,-len(grid[i])-1,-1):
                if grid[i][j]<0:
                    ans+=1
                else:break
        return ans