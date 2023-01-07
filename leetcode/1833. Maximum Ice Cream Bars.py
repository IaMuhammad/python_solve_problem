class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        s, c, d = 0, 0, {}
        for i in costs:
            s += i
            c += 1
            d[i] = True
            if s == coins:
                return c
            elif s > coins:
                if d.get(s - coins):
                    return c - 1
                else:
                    return 0
        return c


a = Solution()
print(a.maxIceCream([7,3,3,6,6,6,10,5,9,2], 56))