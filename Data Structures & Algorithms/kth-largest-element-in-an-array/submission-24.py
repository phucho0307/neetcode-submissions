import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickSelect(left, right):
            if left == right:
                return nums[left]

            pivot = nums[random.randint(left, right)]

            # Three way partition: [<pivot | ==pivot | ?? | >pivot]
            lt, i, gt = left, left, right
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            # After the loop: [left..lt-1] < pivot, [lt..gt] == pivot, [gt+1..right] > pivot
            if target < lt:
                return quickSelect(left, lt - 1)
            elif target > gt:
                return quickSelect(gt + 1, right)
            else:
                return nums[target]   # target is in the ==pivot region

        return quickSelect(0, len(nums) - 1)