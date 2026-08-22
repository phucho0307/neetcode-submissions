class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        biggest = sum(weights)
        smallest = max(weights)
        res = sum(weights)
        
        while smallest <= biggest:
            cap =  (biggest+smallest)//2
            d = 1
            total = 0
            for r in weights:
                total+=r
                if total>cap:
                    total=r
                    d+=1
                if d>days: break
            if d>days: smallest = cap+1
            elif d<=days: 
                res = min(cap, res)
                biggest = cap-1
            
        return res
