class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()
            if i+1< len(candidates) and candidates[i+1] == candidates[i]:
                while i+1< len(candidates) and candidates[i+1] == candidates[i]:
                    i=i+1
            
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res