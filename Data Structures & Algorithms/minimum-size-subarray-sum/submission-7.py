class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minans = 10000000
        l = 0
        r = 0
        cur = 0
        while l <len(nums) and r<len(nums):
            cur += nums[r]
            while cur>= target:
                minans = min(r-l+1, minans)
                cur -= nums[l]
                l+=1
            r+=1
        return minans if minans != 10000000 else 0
        
        