class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        l = len(nums) // 2

        for r in nums:
            cnt[r] +=1
            if cnt[r] > l:
                return r
        return 0

        