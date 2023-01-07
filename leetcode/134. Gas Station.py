class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        cur, pos = 0, 0

        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                pos = i + 1
                cur = 0
        return pos


a = Solution()
print(a.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
