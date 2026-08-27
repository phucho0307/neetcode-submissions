class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 is None and word2 is None: return ""
        first = 0
        second = 0
        res = []
        while first < len(word1) and second < len(word2):
            res.append(word1[first])
            first+=1
            res.append(word2[second])
            second +=1
        if first< len(word1):
            res.append(word1[first:])
        if second < len(word2):
            res.append(word2[second:])
        return "".join(res)