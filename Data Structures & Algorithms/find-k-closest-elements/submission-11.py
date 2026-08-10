class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        l = 0
        r = 0
        res = []
        while r< len(arr) and r-l+1<=k:
            cur = abs(arr[r] - x)
            heapq.heappush(heap, -cur)
            r+=1
        maxNum = -heap[0]
        if r< len(arr): res = arr[l:r]
        else: return arr[l:r]
        while r< len(arr) and r-l+1 > k and abs(arr[r]-x) <= maxNum :
            if abs(arr[r]-x) == maxNum and arr[r] != arr[r-1]: break
            heapq.heappop(heap)
            l+=1
            heapq.heappush(heap,-abs(arr[r]-x))
            res = arr[l:r+1]
            maxNum = -heap[0]
            r+=1
        return res
        

            


