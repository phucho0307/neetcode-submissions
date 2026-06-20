class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue
            l = i+1
            r = len(nums) -1
            while l<r:
                if nums[l]+nums[r] > -nums[i]: r-=1
                elif nums[l]+nums[r] < -nums[i]: l+=1
                else: 
                    res.add((nums[i], nums[l], nums[r]))
                    l+=1
        return [list(triplet) for triplet in res]
            

        