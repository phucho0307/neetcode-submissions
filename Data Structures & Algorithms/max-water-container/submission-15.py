class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0
        right = len(heights)-1
        res =0
        while left<right:
            a = min(heights[left], heights[right]) * (right-left)
            res = max(res,a)
            if heights[left] < heights[right]:
                left+=1
            elif heights[left] > heights[right]:
                right-=1
            else:
                right-=1
                left+=1
        return res
                    
            
            

        