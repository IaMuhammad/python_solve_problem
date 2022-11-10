class StockSpanner:
    def __init__(self):
        self.lis = [(float('-inf'), -1)]
        self.i = -1

    def next(self, price: int) -> int:
        self.i += 1
        if self.lis[-1][0] <= price:
            while self.lis[-1][0] <= price and self.lis[-1][0] != float('-inf'):
                self.lis.pop()
            self.lis.append((price, self.i))
        else:
            self.lis.append((price, self.i))

        k = self.lis[-1][1] - self.lis[-2][1]
        return k

    def __str__(self):
        return f'{self.lis}'
a = StockSpanner()
for i in [1,1,1,2,2,2,2,3,3,3]:
    print(a.next(i), end=' ')