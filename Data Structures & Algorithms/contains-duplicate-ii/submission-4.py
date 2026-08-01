class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = defaultdict(list)
        #1: 0,3, 2:1,..
        a = -1
        for i in range (len(nums)):
            count[nums[i]].append(i)
            if len(count[nums[i]])>1:
                curr = count[nums[i]]
                if abs(curr[len(curr)-2]-i) <= k : a = 1
                else: a = -1
        return a==1
            
        
                


        