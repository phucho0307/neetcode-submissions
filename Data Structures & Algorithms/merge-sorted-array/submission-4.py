class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l1 = len(nums1)-1
        l2 = len(nums2)-1
        while m-1>=0 and n-1>=0:
            if nums1[m-1]>nums2[n-1]:
                nums1[l1] = nums1[m-1]
                m-=1
                l1-=1
            else:
                nums1[l1] = nums2[n-1]
                n-=1
                l1-=1
        while n-1>=0:
            nums1[m] = nums2[m]
            m+=1
            n-=1
