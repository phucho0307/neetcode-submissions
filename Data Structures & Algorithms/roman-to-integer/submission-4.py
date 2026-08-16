class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {}
        dic["I"] = 1
        dic["V"] = 5
        dic["X"] = 10
        dic["L"] = 50
        dic["C"] = 100
        dic["D"] = 500
        dic["M"] = 1000
        res = 0
        for i in range (len(s)):
            if i< len(s)-1 and dic[s[i]] < dic[s[i+1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        return res
                

