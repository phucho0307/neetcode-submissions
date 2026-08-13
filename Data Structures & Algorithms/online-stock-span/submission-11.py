class StockSpanner:

    def __init__(self):
        self.stack =[]

    def next(self, price: int) -> int:
        k=1
        i = len(self.stack)-1
        while i>-1 and price >= self.stack[i]: 
                k+=1
                i -=1
        self.stack.append(price)
        return k



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)