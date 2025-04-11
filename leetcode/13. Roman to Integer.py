class Solution(object):
    def __init__(self):
        self.roman_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        self.other_roman_numbers = {
            'V': 'I',
            'X': 'I',
            'L': 'X',
            'C': 'X',
            'D': 'C',
            'M': 'C',
        }

    def romanToInt(self, s):
        _pre, rtype = '', 0
        for i in s:
            rtype += self.roman_numbers.get(i, 0)
            if self.other_roman_numbers.get(i) == _pre:
                rtype -= self.roman_numbers.get(self.other_roman_numbers.get(i)) * 2

            _pre = i
        print(rtype)


class Solution2(object):
    def __init__(self):
        self.roman_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    def romanToInt(self, s):
        total = i = 0
        while i < len(s):
            if i+1 < len(s) and self.roman_numbers[s[i]] < self.roman_numbers[s[i + 1]]:
                total += self.roman_numbers[s[i + 1]] - self.roman_numbers[s[i]]
                i+=2
            else:
                total += self.roman_numbers[s[i]]
                i+=1
        return total


a = Solution2()
print(a.romanToInt('LVIII'))
