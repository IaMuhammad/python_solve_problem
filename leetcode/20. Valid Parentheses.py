class Solution(object):
    def __init__(self):
        self.scopes = {
            '(': 0,
            '[': 0,
            '{': 0,
            ')': '(',
            ']': '[',
            '}': '{',
        }
        self.last = ''
        self.total = 0

    def isValid(self, s):
        for i in s:
            item = self.scopes[i]
            if type(item) == int:
                self.scopes[i] += 1
                self.total += 1
                self.last += i
            else:
                _ = self.scopes[item]
                if _ == 0 or self.last[-1] != self.scopes[i]:
                    return False
                if self.last[-1] == self.scopes[i]:
                    self.last = self.last[:-1]
                self.total -= 1
                self.scopes[item] -= 1
        return True and self.total == 0


a = Solution()
print(a.isValid("()"))
print(a.isValid("([)]"))
