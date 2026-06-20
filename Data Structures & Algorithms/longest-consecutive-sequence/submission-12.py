class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = set(nums)
        longest = 0
        
        for n in c:                    # iterate values directly
            if n - 1 not in c:         # n starts a sequence
                length = 1
                while n + length in c:
                    length += 1
                longest = max(length, longest)
        
        return longest