class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left<=right:
            mid = int(left + (right-left)/2)
            k = 0
            for b in piles:
                k += b//mid if b%mid==0 else int(b/mid)+1
            if k>h: left = mid+1
            elif k<=h: right = mid
            if left == right: return left
        return mid




        