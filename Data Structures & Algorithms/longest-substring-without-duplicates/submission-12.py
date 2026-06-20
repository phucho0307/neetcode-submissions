class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        a =""
        for i, char in enumerate(s):
            if char not in a:
                a+=char
            else:
                
                if len(res)< len(a):
                    res = a
                a+=char
                g = a.index(char)
                a = a[(g+1):]
                   
        return max(len(a), len(res))                

