class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i, x in enumerate(nums):
            l = target - x
            if l in c: return [c[l], i]
            c[x] = i
        return []
        