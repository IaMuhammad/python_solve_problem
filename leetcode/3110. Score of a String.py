class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = s[0]
        answer = 0
        for i in s[1:]:
            answer += abs(ord(i) - ord(prev))
            prev = i
        return answer
a = Solution()
print(a.scoreOfString('hello'))
print(a.scoreOfString('zaz'))