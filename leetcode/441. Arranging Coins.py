class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        def check(point1, point2):
            return point1[0] <= point2[0] and point1[1] >= point2[0]

        intervals.sort()
        ans = [intervals[0]]
        for i in intervals[1:]:
            if check(ans[-1], i):
                ans[-1] = [min(i[0], ans[-1][0]), max(i[1], ans[-1][1])]
            else:
                ans.append(i)
        return ans
