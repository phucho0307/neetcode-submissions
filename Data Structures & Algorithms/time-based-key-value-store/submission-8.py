class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.map)==0: return ""
        array = self.map[key]
        l = 0
        r = len(array)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if array[m][1] > timestamp:
                r = m-1
            elif array[m][1] <= timestamp:
                l = m+1
                res = array[m][0]
            else: return array[m][0]
        return res
        
        

        



