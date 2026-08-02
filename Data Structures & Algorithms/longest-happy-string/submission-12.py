class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = []
        for cnt, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if cnt != 0:
                heapq.heappush(count, (cnt, char))
        res = ""
        while count:
            curr = heapq.heappop(count)
            if len(res)>1 and curr[1] == res[-1] ==res[-2]:
                #pops alternative, cannot add this one
                if not count:
                    break
                curr2 = heapq.heappop(count)
                res+= curr2[1]
                if curr2[0]+1 != 0:
                    heapq.heappush(count, (curr2[0]+1, curr2[1]))
                heapq.heappush(count, (curr[0], curr[1]))
            else:
                res += curr[1]
                if curr[0]+1 != 0:
                    heapq.heappush(count, (curr[0]+1, curr[1]))

            
        return res

        
        