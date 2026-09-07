class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        right_sum = total_sum - nums[0]
        if left_sum == right_sum:
            return 0

        for i in range (1, len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1
           


        
