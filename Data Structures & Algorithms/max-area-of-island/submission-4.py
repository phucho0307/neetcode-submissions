class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        maxres = 0
        seen = set()
        def dfs(r,c):
            
            if r<0 or c<0 or r>=m or c>=n or grid[r][c] == 0 or (r,c) in seen:
                return 0
            if grid[r][c] == 1:
                seen.add((r,c))
                return 1 + dfs(r,c+1) + dfs(r, c-1) + dfs(r-1,c) + dfs(r+1,c)
            
        for r in range (m):
            for c in range (n):
                if grid[r][c] == 1:
                    maxres = max(maxres, dfs(r,c))
        return maxres


            

