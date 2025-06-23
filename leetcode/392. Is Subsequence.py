class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        string
        """
        index = 0
        for i in s:
            if i in t:
                t = t[t.index(i) + 1:]
            else:
                return False
        return True

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        two pointer
        """
        left = right = 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
                right += 1
            elif right < len(t):
                right += 1
            else:
                return False
        return True


a = Solution()
# print(a.isSubsequence("twn", 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn'))
print(a.isSubsequence('aaaaaa', 'bbaaaa'))
print(a.isSubsequence('abc', 'ahgdcb'))
