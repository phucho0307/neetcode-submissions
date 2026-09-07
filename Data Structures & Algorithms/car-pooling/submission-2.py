class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        cur_pas = 0
        minheap = []
        for pas, start, end in trips:
            while minheap and minheap[0][1] <= start:
                cur_pas -= heapq.heappop(minheap)[0]
            cur_pas += pas
            if cur_pas > capacity:
                return False
            heapq.heappush(minheap, (pas, end))
        return True

