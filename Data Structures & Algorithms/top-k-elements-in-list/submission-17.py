class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for i in range (len(nums)+1)]
        for n, f in counts.items():
            freq[f].append(n)
        res = []
        for g in range (len(freq)-1, 0, -1):
            for l in (freq[g]):
                res.append(l)
                if len(res)==k: return res
        return []
        
            
        