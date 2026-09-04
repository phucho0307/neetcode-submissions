from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
            
        m, n = len(grid), len(grid[0])
        q = deque()
        
        # 1. Add all treasure chests (0s) to the queue
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # 2. Multi-source BFS layer-by-layer
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and only visit unvisited empty rooms
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))