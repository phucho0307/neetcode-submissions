class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        row, col = len(grid), len(grid[0])
        self.perim = 0

        def dfs(i,j):
            if i<0 or j<0 or i>row-1 or j>col-1 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            self.perim = dfs(i,j+1) + dfs(i,j-1) + dfs(i-1,j) + dfs(i+1,j)
            return self.perim
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    dfs(i,j)
        return self.perim