class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = defaultdict(list)
        phone["2"] = ["a", "b", "c"]
        phone["3"] = ["d", "e", "f"]
        phone["4"] = ["g", "h", "i"]
        phone["5"] = ["j", "k", "l"]
        phone["6"] = ["m", "n", "o"]
        phone["7"] = ["p", "q", "r", "s"]
        phone["8"] = ["t", "u", "v"]
        phone["9"] = ["w", "x", "y", "z"]
        res = []
        final = []
        if not digits: return []
        def dfs(k):
            if k >= len(digits):
                final.append("".join(res))
                return
            for r in phone[digits[k]]:
                res.append(r)
                dfs(k+1)
                res.pop()
        dfs(0)
        return final

        
        

        