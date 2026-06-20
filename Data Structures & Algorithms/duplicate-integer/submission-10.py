class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = set()
        for i in nums:
            if i in c: return True
            c.add(i)
        return False