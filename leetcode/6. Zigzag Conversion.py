class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        step = numRows * 2 - 2
        answer = s[::step]
        for i in range(numRows - 1):
            pass
        return answer


a = Solution()
print(a.convert('PAYPALISHIRING', 4))
