class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = {
            'A': 1, 'F': 6, 'K': 11, 'P': 16, 'U': 21, 'Z': 26,
            'B': 2, 'G': 7, 'L': 12, 'Q': 17, 'V': 22,
            'C': 3, 'H': 8, 'M': 13, 'R': 18, 'W': 23,
            'D': 4, 'I': 9, 'N': 14, 'S': 19, 'X': 24,
            'E': 5, 'J': 10, 'O': 15, 'T': 20, 'Y': 25,
        }
        n, i = 0, 1
        for v in columnTitle[::-1]:
            n += d[v] * i
            i *= 26
        return n
