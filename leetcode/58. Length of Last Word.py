class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     """
    #     brute force
    #     """
    #     return len(s.split()[-1])

    def lengthOfLastWord(self, s: str) -> int:
        right, length = len(s) - 1, 0
        latter = True
        while right > -1 and (s[right] != ' ' or latter):
            if s[right] != ' ' and latter:
                latter = False
                length = 0

            length += 1
            right -= 1
        return length


a = Solution()
print(a.lengthOfLastWord("d"))
print(a.lengthOfLastWord("hello world"))
print(a.lengthOfLastWord("hello world "))
