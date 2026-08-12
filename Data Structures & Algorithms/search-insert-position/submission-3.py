class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = 0
        while l<=r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif nums[m]< target:
                l = m+1
            else:
                r = m-1
        return m+1 if nums[m] < target else m