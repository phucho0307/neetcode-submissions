class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {}
        for i,v in enumerate(nums1):
            nums1Idx[v] = i
        res = [-1] * len(nums1)
        stack = []
        for r in nums2:
            while stack and stack[-1] < r:
                idx = nums1Idx[stack[-1]]
                res[idx] = r
                stack.pop()
            if r in nums1Idx:
                stack.append(r)
        return res

        