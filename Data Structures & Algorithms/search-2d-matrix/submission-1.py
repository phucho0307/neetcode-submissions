class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            if self.search(nums, target) != -1: return True
        return False


    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int(left + (right-left)/2)
            if target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
            else: return mid
        return -1    

        