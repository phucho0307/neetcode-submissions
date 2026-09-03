class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m,n = len(grid), len(grid[0])
        cnt = 0

        def dfs(r,c):
            if r<0 or c<0 or r>m-1 or c>n-1 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range (m):
            for c in range (n):
                if grid[r][c]=="1":
                    cnt+=1
                    dfs(r,c)
        return cnt