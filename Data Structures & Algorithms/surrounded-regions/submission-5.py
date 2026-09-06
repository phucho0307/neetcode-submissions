class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        m = len(board)
        n = len(board[0])
        edge_cnt = set()
        for i in range (n):
            if board[0][i] == "O":
                edge_cnt.add((0,i))
            if board[m-1][i] == "O":
                edge_cnt.add((m-1,i))
        for k in range (m):
            if board[k][0] == "O":
                edge_cnt.add((k,0))
            if board[k][n-1] == "O":
                edge_cnt.add((k,n-1))
        q = deque(edge_cnt)
        dirs = [(0,1), (-1,0), (1,0), (0,-1)]
        while q:
            r,c = q.popleft()
            for nr, nc in dirs:
                if 0<= r+nr < m and 0<= c+nc < n and board[r+nr][c+nc] == "O" and (r+nr, c+nc) not in edge_cnt:
                    edge_cnt.add((r+nr, c+nc))
                    q.append((r+nr, c+nc))
        for r in range (m):
            for c in range (n):
                if board[r][c] == "O" and (r, c) not in edge_cnt:
                    board[r][c] = "X"



# xoxx
# oxox
# xoxo
# oxox



        

